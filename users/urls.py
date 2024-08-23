from django.urls import include
from .views import UserCreateAPIView, UserListAPIView, UserRetrieveUpdateDestroyAPIView, DonationCreateAPIView
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path("donation/", DonationCreateAPIView.as_view(), name='donation'),
]
