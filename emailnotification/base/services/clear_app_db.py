import logging
from base.models.EmailNotification import EmailNotification

logger = logging.getLogger()

def clear_app_db():
    global logger
    EmailNotification.objects.all().delete()
    logger.info("Successfully cleared the app database")