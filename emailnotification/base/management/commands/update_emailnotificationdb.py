from django.core.management.base import BaseCommand, CommandParser
from django.core.mail import send_mail
from django.db.models import Q
from base.models import EmailNotification
from base.openprojectdb_models import WorkPackages
import datetime

class Command(BaseCommand):
    
    help = 'This is a test command to see if it successfully adds a new row of data to the db'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--clearappdb', type=bool, help='Clear the application database')
    
    def handle(self, *args, **options):
        clearAppDB = options['clearappdb']

        if(clearAppDB):
            EmailNotification.objects.all().delete()
            print("Successfully cleared the app database")
        else:
            current_date = datetime.date.today()
            workpackages = WorkPackages.objects.using('openprojectdb').all()
            for workpackage in workpackages:
                if(workpackage.due_date != None and current_date > workpackage.due_date):
                    delta = current_date - workpackage.due_date
        
                    print(f"This task is overdue. Task id: {workpackage.id}. Overdue {delta.days} days.")
            #send_mail("Hello from django ", "Hello world", "Django Custom Command", ["serhanturgul2@gmail.com"], fail_silently=False,)
            self.updateAppDB()

    def updateAppDB(self):
        closed_status_id = 12
        active_work_packages = WorkPackages.objects.using('openprojectdb').exclude(Q(status=closed_status_id) | Q(due_date__isnull=True))
        for workpackage in active_work_packages:
            if not EmailNotification.objects.filter(work_package_id=workpackage.id).exists():
                EmailNotification.objects.create(work_package_id=workpackage.id, due_date=workpackage.due_date, mail_sent=False)
            else:
                print("Entry exists")
    

