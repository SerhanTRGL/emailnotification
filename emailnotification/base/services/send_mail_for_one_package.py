from django.core.mail import send_mail
from django.utils import timezone
import logging
import datetime

closed_status_id = 12
logger = logging.getLogger()

def send_mail_for_one_package(email_notification):
    current_date = datetime.date.today()
    if current_date > email_notification.due_date:
        recipient_list = list(set([email_notification.assignee_mail, email_notification.author_mail, email_notification.responsible_mail]))
        recipient_list = [email_address for email_address in recipient_list if email_address is not None]
        subject = f"{email_notification.work_package_id} Numaralı İş Paketinin Teslim Tarihi Geçti!"
        message = f"{email_notification.work_package_id} Numaralı iş paketinin teslim tarihi geçmiş bulunmakta\n Durum iş paketinin sorumlularına ve yaratıcısına bildirilmiştir."
        sender = "OpenProject Management"
        send_mail(subject, message, sender, recipient_list, fail_silently=False)
        email_notification.mail_sent = True
        email_notification.mail_sent_date = timezone.now()
        email_notification.save()