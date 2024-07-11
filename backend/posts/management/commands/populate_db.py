from ...models import Post
from django.core.management.base import BaseCommand

from .get_data import get_data
    
class Command(BaseCommand):
    help = "Populates the database."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Started database population process..."))
        if Post.objects.all().exists():
            self.stdout.write(self.style.SUCCESS("Database has already been populated. Cancelling the operation."))
            return
        print("Getting branded posts")
        get_data(cursor='', post_type='branded_without_fans')
        print("Getting stadium posts")
        get_data(cursor='', post_type='stadium')
        print("Getting fan posts")
        get_data(cursor='', post_type='fan')
        
        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))