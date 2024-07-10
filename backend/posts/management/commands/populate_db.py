from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from ...get_data import get_data
    
class Command(BaseCommand):
    help = "Populates the database with some testing data."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Started database population process..."))
        
        get_data(cursor='', post_type='fan')
        
        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))