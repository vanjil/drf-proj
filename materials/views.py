from rest_framework import viewsets
from .models import Kurs, Urok, Payment
from .serializer import KursSerializer, UrokSerializer, PaymentSerializer
from .permissions import IsOwnerOrModerator, IsModeratorOrReadOnly

class KursViewSet(viewsets.ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            self.permission_classes = [IsOwnerOrModerator]
        elif self.action == 'list' or self.action == 'retrieve':
            self.permission_classes = [IsModeratorOrReadOnly]
        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return Kurs.objects.all()
        return Kurs.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UrokViewSet(viewsets.ModelViewSet):
    queryset = Urok.objects.all()
    serializer_class = UrokSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            self.permission_classes = [IsOwnerOrModerator]
        elif self.action == 'list' or self.action == 'retrieve':
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

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            self.permission_classes = [IsOwnerOrModerator]
        elif self.action == 'list' or self.action == 'retrieve':
            self.permission_classes = [IsModeratorOrReadOnly]
        return [permission() for permission in self.permission_classes]
