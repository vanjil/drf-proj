from rest_framework.serializers import ModelSerializer, SerializerMethodField
from materials.models import Kurs, Urok
from users.models import Payment

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class UrokSerializer(ModelSerializer):
    class Meta:
        model = Urok
        fields = '__all__'

class UrokDetaileSerializer(ModelSerializer):
    urok_whith_same_kurs = SerializerMethodField()

    def get_urok_whith_same_kurs(self, urok):
        same_kurs_uroki = Urok.objects.filter(kurs=urok.kurs)
        return UrokSerializer(same_kurs_uroki, many=True).data

    class Meta:
        model = Urok
        fields = ("name", "description", "image", "video_link", "urok_whith_same_kurs")

class KursSerializer(ModelSerializer):
    uroki = UrokSerializer(many=True, read_only=True)
    urok_count = SerializerMethodField()
    payments = SerializerMethodField()

    def get_urok_count(self, obj):
        return obj.uroki.count()

    def get_payments(self, obj):

        payments = Payment.objects.filter(paid_course=obj)
        return PaymentSerializer(payments, many=True).data

    class Meta:
        model = Kurs
        fields = ['id', 'name', 'description', 'image', 'uroki', 'urok_count', 'payments']
