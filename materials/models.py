from django.db import models
from django.conf import settings

class Kurs(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса", blank=True, null=True)
    image = models.ImageField(verbose_name="Картинка", blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='kurs', null=True, blank=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

class Urok(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название урока", help_text="Дайте название урока")
    description = models.TextField(verbose_name="Описание урока", help_text="Опишите основные материалы и условия урока")
    image = models.ImageField(verbose_name="Картинка", blank=True, null=True, help_text="Загрузите картинку")
    video_link = models.URLField(verbose_name="Ссылка на видео", help_text="Добавьте ссылку на урок")
    kurs = models.ForeignKey(Kurs, related_name='uroki', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='uroki', null=True, blank=True)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('card', 'Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='material_payments')
    payment_date = models.DateTimeField(auto_now_add=True)
    paid_course = models.ForeignKey(Kurs, null=True, blank=True, on_delete=models.CASCADE, related_name='material_payments')
    paid_lesson = models.ForeignKey(Urok, null=True, blank=True, on_delete=models.CASCADE, related_name='material_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
