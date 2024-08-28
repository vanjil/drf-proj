from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('drf-proj')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.beat_schedule = {
    'block-inactive-users-every-day': {
        'task': 'users.tasks.block_inactive_users',
        'schedule': crontab(hour=0, minute=0),
    },
}

app.conf.timezone = 'UTC'
