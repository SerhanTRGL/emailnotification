from django.core.management.base import BaseCommand, CommandParser
from base.services.clear_app_db import clear_app_db
from base.services.sync_databases import sync_databases
from base.services.send_all_mails import send_all_mails 

class Command(BaseCommand):

    closed_status_id = 12
    help = 'Command that checks openproject database to send mails for overdue workpackages'
    

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--clearappdb', action='store_true', help='Clear the application database')
        parser.add_argument('--nothreads', action='store_true', help='Send emails using multiple threads')
    
    def handle(self, *args, **options):
        can_clear_app_db = options['clearappdb']
        no_threads = options['nothreads']

        if can_clear_app_db:
            clear_app_db()
        else:
            sync_databases()
            send_all_mails(no_threads)
        

