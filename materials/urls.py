from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.views import UrokViewSet, KursCreateApiView, KursUpdateApiView, KursDestroyApiView, KursListApiView, KursRetrieveApiView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("urok", UrokViewSet)

urlpatterns = [
    path("kurs/", KursListApiView.as_view(), name="kurs_list"),
    path("kurs/<int:pk>/", KursRetrieveApiView.as_view(), name="kurs_retrieve"),
    path("kurs/create/", KursCreateApiView.as_view(), name="kurs_create"),
    path("kurs/<int:pk>/update/", KursUpdateApiView.as_view(), name="kurs_update"),
    path("kurs/<int:pk>/delete/", KursDestroyApiView.as_view(), name="kurs_destroy")
]

urlpatterns += router.urls
