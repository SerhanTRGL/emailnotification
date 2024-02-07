from django.db import models

class EmailNotification(models.Model):
    work_package_id = models.BigIntegerField()
    due_date = models.DateField()
    mail_sent = models.BooleanField()

    class Meta:
        app_label = 'base'
        