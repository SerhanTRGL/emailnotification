from celery import shared_task
import base.service

@shared_task(name='sendemail_task', ignore_result=True)
def sendemail_task():
    base.service.syncDatabases()
    base.service.sendMails(no_threads=False)