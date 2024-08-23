from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payment, Donation
from .serializer import PaymentSerializer, DonationSerializer
from .filters import PaymentFilter
from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer
from rest_framework import permissions

from .service import convert_rub_to_dollars, create_stripe_prise, create_stripe_session


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserPaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class IsModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Проверка, является ли пользователь модератором
        return request.user.groups.filter(name='Moderators').exists()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Модераторы могут редактировать, но не удалять
        if request.user.groups.filter(name='Moderators').exists():
            return True
        return False

class DonationCreateAPIView(generics.CreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        amount_in_dollar = convert_rub_to_dollars(payment.amount)
        price = create_stripe_prise(amount_in_dollar)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link