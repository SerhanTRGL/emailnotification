from celery import shared_task
from base.services.sync_databases import sync_databases
from base.services.send_all_mails import send_all_mails

@shared_task(name='sendemail_task', ignore_result=True)
def sendemail_task():
    sync_databases()
    send_all_mails(no_threads=False)