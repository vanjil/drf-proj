from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Указываем Django настройки для конфигурации Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('drf-proj')

# Загружаем настройки из config.settings с префиксом CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находит задачи (tasks) в приложениях Django
app.autodiscover_tasks()
