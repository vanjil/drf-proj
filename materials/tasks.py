from django.core.mail import send_mail
from django.conf import settings
from .models import Subscription, Kurs


from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from celery import shared_task

User = get_user_model()

@shared_task
def block_inactive_users():
    inactive_period = timedelta(days=180)  # Задаем период неактивности
    inactive_users = User.objects.filter(last_login__lt=timezone.now() - inactive_period, is_active=True)

    for user in inactive_users:
        user.is_active = False
        user.save()


@shared_task
def send_course_update_email(course_id):
    course = Kurs.objects.get(id=course_id)
    subscriptions = Subscription.objects.filter(kurs=course)

    for subscription in subscriptions:
        user = subscription.user
        send_mail(
            'Обновление курса!',
            f'Привет, {user.username},\n\n Курс "{course.name}" был обновлен.\n\nс лучшими пожеланиями,\nВаш преподаватель',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )



