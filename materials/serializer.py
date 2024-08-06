from rest_framework.serializers import ModelSerializer

from materials.models import Urok, Kurs


class UrokSerializer(ModelSerializer):
    class Meta:
        model = Urok
        fields = '__all__'


class KursSerializer(ModelSerializer):
    class Meta:
        model = Kurs
        fields = '__all__'
