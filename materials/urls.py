from django.views.generic import TemplateView

from materials.views import KursCreateApiView, KursUpdateApiView, KursDestroyApiView, KursListApiView, KursRetrieveApiView
from materials.apps import MaterialsConfig
from django.urls import  include

from rest_framework.routers import DefaultRouter
from .views import KursViewSet, UrokViewSet, PaymentViewSet
from django.urls import path

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'kurs', KursViewSet)
router.register(r'urok', UrokViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('kurs/', KursListApiView.as_view(), name='kurs_list'),
    path('kurs/<int:pk>/', KursRetrieveApiView.as_view(), name='kurs_retrieve'),
    path('kurs/create/', KursCreateApiView.as_view(), name='kurs_create'),
    path('kurs/<int:pk>/update/', KursUpdateApiView.as_view(), name='kurs_update'),
    path('kurs/<int:pk>/delete/', KursDestroyApiView.as_view(), name='kurs_destroy'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

]

