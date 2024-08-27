from rest_framework import viewsets
from .models import Urok, Subscription, Kurs, Payment
from .serializer import KursSerializer, UrokSerializer, PaymentSerializer
from .permissions import IsOwnerOrModerator, IsModeratorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .paginators import CustomPageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Импорт функций для работы с Stripe и создания записей о платежах
from .payment_services import create_product, create_price, create_checkout_session, create_payment
from .tasks import send_course_update_email

class KursViewSet(viewsets.ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsOwnerOrModerator]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [IsModeratorOrReadOnly]
        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name='moderators').exists():
                return Kurs.objects.all()
            return Kurs.objects.filter(user=self.request.user)
        else:
            return Kurs.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        super().perform_update(serializer)
        # Запускаем задачу для отправки письма
        send_course_update_email.delay(serializer.instance.id)

class CreateCheckoutSessionView(APIView):
    def post(self, request):
        kurs_id = request.data.get('kurs_id')
        user_id = request.data.get('user_id')
        success_url = request.data.get('success_url')
        cancel_url = request.data.get('cancel_url')

        if not all([kurs_id, user_id, success_url, cancel_url]):
            return Response({'error': 'Missing parameters'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            kurs = Kurs.objects.get(id=kurs_id)
        except Kurs.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        # Создание продукта и цены
        product = create_product(kurs.name, kurs.description)
        price = create_price(product.id, kurs.price)

        # Создание сессии
        session = create_checkout_session(price.id, success_url, cancel_url)

        # Создание записи о платеже
        create_payment(kurs_id, user_id, kurs.price)

        return Response({'url': session.url}, status=status.HTTP_200_OK)

class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course_id')

        if not course_id:
            return Response({'error': 'Missing course_id parameter'}, status=status.HTTP_400_BAD_REQUEST)

        course_item = get_object_or_404(Kurs, id=course_id)
        subs_item = Subscription.objects.filter(user=user, kurs=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'Subscription removed'
        else:
            Subscription.objects.create(user=user, kurs=course_item)
            message = 'Subscription added'

        return Response({"message": message})

class UrokViewSet(viewsets.ModelViewSet):
    queryset = Urok.objects.all()
    serializer_class = UrokSerializer
    pagination_class = CustomPageNumberPagination

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsOwnerOrModerator]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [IsModeratorOrReadOnly]
        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return Urok.objects.all()
        return Urok.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = CustomPageNumberPagination

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsOwnerOrModerator]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [IsModeratorOrReadOnly]
        return [permission() for permission in self.permission_classes]
