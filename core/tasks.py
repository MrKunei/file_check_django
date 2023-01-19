from celery import shared_task
from django.core.mail import send_mail
from django.db.models import Q

from .models import File


@shared_task
def verify_file():
    files = File.objects.filter(Q(status=File.UPDATED_STATUS) | Q(status=File.NEW_STATUS))
    for file in files:
        file.status = File.VERIFIED_STATUS
        file.save()


@shared_task
def send_log_email():
    pass

