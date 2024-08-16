from rest_framework import viewsets
from .models import Kurs, Urok, Payment
from .serializer import KursSerializer, UrokSerializer, PaymentSerializer
from .permissions import IsOwnerOrModerator

class KursViewSet(viewsets.ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    permission_classes = [IsOwnerOrModerator]

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return Kurs.objects.all()
        return Kurs.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UrokViewSet(viewsets.ModelViewSet):
    queryset = Urok.objects.all()
    serializer_class = UrokSerializer
    permission_classes = [IsOwnerOrModerator]

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return Urok.objects.all()
        return Urok.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsOwnerOrModerator]
