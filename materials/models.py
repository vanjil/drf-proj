from django.db import models


class Kurs(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название курса", help_text="Дайте название курса"
    )
    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Опишите основные материалы и условия курса",
        blank=True, null=True,
    )
    image = models.ImageField(
        verbose_name="картинка", blank=True, null=True, help_text="Загрузите картинку"
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Urok(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название урока", help_text="Дайте название урока"
    )
    description = models.TextField(
        verbose_name="Описание урока",
        help_text="Опишите основные материалы и условия урока"
    )
    image = models.ImageField(
        verbose_name="картинка", blank=True, null=True, help_text="Загрузите картинку"
    )
    video_link = models.URLField(
        verbose_name="Ссылка на видео", help_text="Добавьте ссылку на урок"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
