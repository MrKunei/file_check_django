import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'verify-file-every-five-minutes': {
        'task': 'core.tasks.verify_file',
        'schedule': crontab(minute='*/1'),
    },

    'check-log-and-send-mail': {
        'task': 'core.tasks.send_log_email',
        'schedule': crontab(minute='*/3'),
    },

}