from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from posts.models import Post
import requests
import os
from dotenv import load_dotenv
load_dotenv()

from .data import data

from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
    
class Command(BaseCommand):
    help = "Populates the database with some testing data."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Started database population process..."))
        
        # if User.objects.filter(username="mike13").exists():
        #     self.stdout.write(self.style.SUCCESS("Database has already been populated. Cancelling the operation."))
        #     return

        # # Create users
        # mike = User.objects.create_user(username="mike13", password="really_strong_password123")
        # mike.first_name = "Mike"
        # mike.last_name = "Smith"
        # mike.save()

        # jess = User.objects.create_user(username="jess_", password="really_strong_password123")
        # jess.first_name = "Jess"
        # jess.last_name = "Brown"
        # jess.save()

        # johnny = User.objects.create_user(username="johnny", password="really_strong_password123")
        # johnny.first_name = "Johnny"
        # johnny.last_name = "Davis"
        # johnny.save()

        # Create posts
        for each in data['posts']:
            sentiment = sentiment_pipeline(each['original_description'])
            post = Post.objects.create(
                author = each['author'],
                date = each['date'],
                timestamp = each['timestamp'],
                description = each['original_description'],
                url = each['url'],
                
                engagement = each['engagement'],
                
                public_impressions = each['public_impressions'],
                estimated_views = each['estimated_views'],
                liked_count = each['liked_count'],
                replied_count = each['replied_count'],
                reposted_count = each['reposted_count'],
                
                sentiment_label = sentiment[0]['label'],
                sentiment_score = sentiment[0]['score'] 
            )
            post.save()

        # response = requests.get(os.getenv("API"), headers={'authorization': 'Bearer ' + os.getenv("TOKEN")})
        # print(response, response.json())
        

        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))