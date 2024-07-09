from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.CharField(null=True, blank=True)
    date = models.TextField(null=True, blank=True)
    timestamp = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(null=True, blank=True)
    
    engagement = models.IntegerField(null=True, blank=True)

    public_impressions = models.IntegerField(null=True, blank=True)
    estimated_views = models.IntegerField(null=True, blank=True)
    liked_count = models.IntegerField(null=True, blank=True)
    replied_count = models.IntegerField(null=True, blank=True)
    reposted_count = models.IntegerField(null=True, blank=True)

    sentiment_label = models.CharField(null=True, blank=True)
    sentiment_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Post: {self.description}"