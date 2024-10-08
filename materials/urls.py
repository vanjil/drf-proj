from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KursViewSet, UrokViewSet, PaymentViewSet, SubscriptionView, CreateCheckoutSessionView

app_name = 'materials'

router = DefaultRouter()
router.register(r'kurs', KursViewSet)
router.register(r'urok', UrokViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('subscription/', SubscriptionView.as_view(), name='subscription'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),

]
