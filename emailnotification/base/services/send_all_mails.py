import logging
import time
from base.models import EmailNotification
from concurrent.futures import ThreadPoolExecutor
from . import send_mail_for_one_package


logger = logging.getLogger()
def send_all_mails(no_threads):
    global logger

    start = time.time()
    email_notifications = EmailNotification.objects.exclude(is_marked_as_closed=True).exclude(mail_sent=True)

    if no_threads:
        for email_notification in email_notifications:
            send_mail_for_one_package(email_notification)
    else:
        with ThreadPoolExecutor(max_workers=None) as executor:
            executor.map(send_mail_for_one_package, email_notifications)

    end = time.time()
    logger.info(f"Time elapsed sending emails: {end-start} seconds.")