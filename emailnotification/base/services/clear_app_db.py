from base.models import EmailNotification

def clearAppDB():
    global logger
    EmailNotification.objects.all().delete()
    logger.info("Successfully cleared the app database")