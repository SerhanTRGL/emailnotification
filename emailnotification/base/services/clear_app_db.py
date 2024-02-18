from base.models import EmailNotification

def clear_app_db():
    global logger
    EmailNotification.objects.all().delete()
    logger.info("Successfully cleared the app database")