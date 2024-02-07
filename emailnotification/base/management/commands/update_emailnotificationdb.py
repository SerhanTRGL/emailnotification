from django.core.management.base import BaseCommand
from base.models import EmailNotification
from base.openprojectdb_models import WorkPackages

class Command(BaseCommand):
    help = 'This is a test command to see if it successfully adds a new row of data to the db'


    def handle(self, *args, **options):
        newData = EmailNotification(work_package_id=4,
                                    mail_sent=True,
                                    due_date='2025-05-05')
        workpackages = WorkPackages.objects.using('openprojectdb').all()
        for workpackage in workpackages:
            print(workpackage)
        newData.save()