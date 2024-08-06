from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from materials.models import Urok, Kurs
from materials.serializer import UrokSerializer, KursSerializer


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
