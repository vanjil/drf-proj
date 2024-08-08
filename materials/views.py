from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from materials.models import Urok, Kurs
from materials.serializer import UrokSerializer, KursSerializer

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payment
from .serializer import PaymentSerializer
from .filters import PaymentFilter

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PaymentFilter


class UrokViewSet(ModelViewSet):
    queryset = Urok.objects.all()
    serializer_class = UrokSerializer


class KursCreateApiView(CreateAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer


class KursListApiView(ListAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer


class KursRetrieveApiView(RetrieveAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer

class KursUpdateApiView(UpdateAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer

class KursDestroyApiView(DestroyAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer


class KursViewSet(viewsets.ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
