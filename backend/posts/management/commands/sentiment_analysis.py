from django.core.management.base import BaseCommand
from ...models import Post
from transformers import pipeline

class Command(BaseCommand):
    help = "Run sentiment analysis"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Started sentiment analysis..."))
        posts = Post.objects.all()
        sentiment_pipeline = pipeline('sentiment-analysis', model="cardiffnlp/twitter-roberta-base-sentiment-latest")
        for post in posts:
            sentiment = sentiment_pipeline(post.description)
            post.sentiment_label = sentiment[0]['label']
            post.sentiment_score = sentiment[0]['score']
            post.save()
        self.stdout.write(self.style.SUCCESS("Successfully finished the analysis."))
