from rest_framework import viewsets
from .models import Urok, Payment, Kurs, Subscription
from .serializer import KursSerializer, UrokSerializer, PaymentSerializer
from .permissions import IsOwnerOrModerator, IsModeratorOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .paginators import CustomPageNumberPagination

class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course_id')
        course_item = get_object_or_404(Kurs, id=course_id)
        subs_item = Subscription.objects.filter(user=user, kurs=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка удалена'
        else:
            Subscription.objects.create(user=user, kurs=course_item)
            message = 'Подписка добавлена'

        return Response({"message": message})

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
