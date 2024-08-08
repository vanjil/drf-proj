import django_filters
from .models import Payment

class PaymentFilter(django_filters.FilterSet):
    payment_date = django_filters.DateTimeFilter(field_name='payment_date', lookup_expr='exact')
    kurs = django_filters.NumberFilter(field_name='paid_course', lookup_expr='exact')
    urok = django_filters.NumberFilter(field_name='paid_lesson', lookup_expr='exact')
    payment_method = django_filters.ChoiceFilter(field_name='payment_method', choices=Payment.PAYMENT_METHODS)
    ordering = django_filters.OrderingFilter(
        fields=(
            ('payment_date', 'payment_date'),
        )
    )

    class Meta:
        model = Payment
        fields = ['payment_date', 'paid_course', 'paid_lesson', 'payment_method']
