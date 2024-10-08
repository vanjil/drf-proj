from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from materials.models import Kurs, Urok
from .managers import CustomUserManager

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_payments')
    payment_date = models.DateTimeField(auto_now_add=True)
    paid_course = models.ForeignKey(Kurs, null=True, blank=True, on_delete=models.CASCADE, related_name='user_payments')
    paid_lesson = models.ForeignKey(Urok, null=True, blank=True, on_delete=models.CASCADE, related_name='user_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[('card', 'Card'), ('paypal', 'PayPal')])

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.user} - {self.amount} - {self.payment_date}"

class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название города")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name

class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )

    phone = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Введите телефон",
    )

    city = models.ForeignKey(
        City,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Город",
        help_text="Город проживания"
    )

    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите фото",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Donation(models.Model):
    amount = models.PositiveIntegerField(
        verbose_name="Сумма пожертвования",
        help_text="Укажите сумму пожертвования",
    )
    session_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="ID сессии",
        help_text="Укажите ID сессии",
    )
    link = models.URLField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="ссылка на оплату",
        help_text="Укажите ссылку на оплату",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
    )

    class Meta:
        verbose_name = "Пожертвование"
        verbose_name_plural = "Пожертвования"

    def __str__(self):
        return self.amount