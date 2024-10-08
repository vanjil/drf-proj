from rest_framework import serializers
from .models import Kurs, Urok, Subscription
from users.models import Payment
from .validators import validate_youtube_url

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class UrokSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField(validators=[validate_youtube_url])
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Urok
        fields = '__all__'

class UrokDetaileSerializer(serializers.ModelSerializer):
    urok_whith_same_kurs = serializers.SerializerMethodField()

    def get_urok_whith_same_kurs(self, urok):
        same_kurs_uroki = Urok.objects.filter(kurs=urok.kurs)
        return UrokSerializer(same_kurs_uroki, many=True).data

    class Meta:
        model = Urok
        fields = ("name", "description", "image", "video_link", "urok_whith_same_kurs")

class KursSerializer(serializers.ModelSerializer):
    uroki = UrokSerializer(many=True, read_only=True)
    urok_count = serializers.SerializerMethodField()
    payments = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.username')
    is_subscribed = serializers.SerializerMethodField()

    def get_urok_count(self, obj):
        return obj.uroki.count()

    def get_payments(self, obj):
        payments = Payment.objects.filter(paid_course=obj)
        return PaymentSerializer(payments, many=True).data

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user, kurs=obj).exists()

    class Meta:
        model = Kurs
        fields = ['id', 'name', 'description', 'image', 'uroki', 'urok_count', 'payments', 'user', 'is_subscribed']
