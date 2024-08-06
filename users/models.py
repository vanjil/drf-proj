from django.contrib.auth.models import AbstractUser
from django.db import models


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

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
