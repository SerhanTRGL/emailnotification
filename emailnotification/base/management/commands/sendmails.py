from django.core.management.base import BaseCommand, CommandParser
import base.service

class Command(BaseCommand):

    closed_status_id = 12
    help = 'Command that checks openproject database to send mails for overdue workpackages'
    

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--clearappdb', action='store_true', help='Clear the application database')
        parser.add_argument('--nothreads', action='store_true', help='Send emails using multiple threads')
    
    def handle(self, *args, **options):
        clear_app_db = options['clearappdb']
        no_threads = options['nothreads']

        if clear_app_db:
            base.service.clearAppDB()
        else:
            base.service.syncDatabases()
            base.service.sendMails(no_threads)
        

