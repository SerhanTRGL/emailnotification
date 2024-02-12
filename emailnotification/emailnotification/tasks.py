from celery import shared_task
from django.core.management import call_command

@shared_task
def sendmails():
    call_command('sendmails')