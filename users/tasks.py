from celery import shared_task
from django.utils import timezone
from django.contrib.auth import get_user_model
from dateutil.relativedelta import relativedelta

@shared_task
def block_inactive_users():
    month_ago = timezone.now() - relativedelta(months=1)
    User = get_user_model()
    qs = User.objects.filter(last_login__lt=month_ago, is_active=True)
    qs.update(is_active=False)
