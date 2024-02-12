from django.core.management.base import BaseCommand, CommandParser
from django.core.mail import send_mail
from django.db.models import Q
from base.models import EmailNotification
from base.openprojectdb_models import WorkPackages
from base.openprojectdb_models import Users
import datetime
from django.utils import timezone
import time
from concurrent.futures import ThreadPoolExecutor
import logging

class Command(BaseCommand):
    
    help = 'This is a test command to see if it successfully adds a new row of data to the db'
    closed_status_id = 12
    logger = logging.getLogger()
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--clearappdb', action='store_true', help='Clear the application database')
        parser.add_argument('--nothreads', action='store_true', help='Send emails using multiple threads')
    
    def handle(self, *args, **options):
        clear_app_db = options['clearappdb']
        no_threads = options['nothreads']

        if clear_app_db:
            self.clearAppDB()
        else:
            self.syncDatabases()
            self.sendMails(no_threads)
        
    def syncDatabases(self):
        start = time.time()

        current_date = datetime.date.today()
        active_work_packages = WorkPackages.objects.using('openprojectdb').exclude(Q(status=self.closed_status_id) | Q(due_date__isnull=True))

        #Loop below only adds new entries of packages that are not marked as closed, or updates the ones that are still
        #not closed.
        for work_package in active_work_packages:
            if not EmailNotification.objects.filter(work_package_id=work_package.id).exists():
                email_notification = EmailNotification(work_package_id=work_package.id, due_date=work_package.due_date)

                #print(f"Work_package_id: {work_package.id} author_id: {work_package.author_id} responsible_id: {work_package.responsible_id} assigned_to_id: {work_package.assigned_to_id}")

                if work_package.author_id != None:
                    if Users.objects.using('openprojectdb').filter(Q(id=work_package.author_id) & Q(mail__isnull=False)).exists():
                        email_notification.author_mail = Users.objects.using('openprojectdb').get(id=work_package.author_id).mail

                if work_package.responsible_id != None:
                    if Users.objects.using('openprojectdb').filter(Q(id=work_package.responsible_id) & Q(mail__isnull=False)).exists():
                        email_notification.responsible_mail = Users.objects.using('openprojectdb').get(id=work_package.responsible_id).mail
                
                if work_package.assigned_to_id != None:
                    if Users.objects.using('openprojectdb').filter(Q(id=work_package.assigned_to_id) & Q(mail__isnull=False)).exists():
                        email_notification.assignee_mail = Users.objects.using('openprojectdb').get(id=work_package.assigned_to_id).mail
                
                email_notification.save()
            else: # Work package already exists in app db
                email_notification = EmailNotification.objects.get(work_package_id=work_package.id)
                email_notification.due_date = work_package.due_date
                email_notification.is_marked_as_closed = False #If a closed package can reach this line, it must be reopened

                if work_package.author_id != None:
                    if Users.objects.using('openprojectdb').filter(Q(id=work_package.author_id) & Q(mail__isnull=False)).exists():
                        email_notification.author_mail = Users.objects.using('openprojectdb').get(id=work_package.author_id).mail

                if work_package.responsible_id != None:
                    if Users.objects.using('openprojectdb').filter(Q(id=work_package.responsible_id) & Q(mail__isnull=False)).exists():
                        email_notification.responsible_mail = Users.objects.using('openprojectdb').get(id=work_package.responsible_id).mail
                    
                if work_package.assigned_to_id != None:
                    if Users.objects.using('openprojectdb').filter(Q(id=work_package.assigned_to_id) & Q(mail__isnull=False)).exists():
                        email_notification.assignee_mail = Users.objects.using('openprojectdb').get(id=work_package.assigned_to_id).mail

                if email_notification.mail_sent and work_package.due_date >= current_date: #If mail is sent but due date is changed to a future date
                    email_notification.mail_sent = False

                email_notification.save()

        email_notifications = EmailNotification.objects.all()

        for email_notification in email_notifications:
            if email_notification.is_marked_as_closed:
                if WorkPackages.objects.using('openprojectdb').filter(id=email_notification.work_package_id).exists():
                    work_package = WorkPackages.objects.using('openprojectdb').get(id=email_notification.work_package_id)
                    if work_package.status_id != self.closed_status_id:
                        email_notification.is_marked_as_closed = False
                        email_notification.save()
            else:
                #Workpackage exists in app db but not in the openprojectdb, no need
                #to send email in this case
                if not WorkPackages.objects.using('openprojectdb').filter(id=email_notification.work_package_id).exists(): 
                    email_notification.is_marked_as_closed = True 
                    email_notification.save()

        end = time.time()
        self.logger.info(f"Time elapsed syncing databases: {end-start} seconds.")

    def sendMails(self, no_threads):
        start = time.time()
        
        email_notifications = EmailNotification.objects.exclude(is_marked_as_closed=True).exclude(mail_sent=True)
        if no_threads:
            for email_notification in email_notifications:
                self.sendMailForOnePackage(email_notification)
        else:
            with ThreadPoolExecutor(max_workers=None) as executor:
                executor.map(self.sendMailForOnePackage, email_notifications)

        end = time.time()
        self.logger.info(f"Time elapsed sending emails: {end-start} seconds.")

    def sendMailForOnePackage(self, email_notification):
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

    def clearAppDB(self):
        EmailNotification.objects.all().delete()
        self.logger.info("Successfully cleared the app database")
    

