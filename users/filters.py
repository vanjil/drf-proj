import django_filters
from .models import Payment

class PaymentFilter(django_filters.FilterSet):
    class Meta:
        model = Payment
        fields = ['user', 'paid_course', 'paid_lesson', 'payment_method']
