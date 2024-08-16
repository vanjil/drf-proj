from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KursViewSet, UrokViewSet, PaymentViewSet

app_name = 'materials'

router = DefaultRouter()
router.register(r'kurs', KursViewSet)
router.register(r'urok', UrokViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
