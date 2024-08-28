from django.core.mail import send_mail
from django.conf import settings
from .models import Subscription, Kurs
from celery import shared_task



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



