from django.db import models

class EmailNotification(models.Model):
    work_package_id = models.BigIntegerField()
    due_date = models.DateField()
    author_mail = models.CharField(default=None, null=True)
    responsible_mail = models.CharField(default=None, null=True)
    assignee_mail = models.CharField(default=None, null=True)
    mail_sent = models.BooleanField(default=False)
    mail_sent_date = models.DateTimeField(default=None, null=True)
    is_marked_as_closed = models.BooleanField(default=False)

    class Meta:
        app_label = 'base'
        