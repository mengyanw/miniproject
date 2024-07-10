from django.db import models

# Create your models here.

class Post(models.Model):
    medium_id = models.CharField(primary_key=True)

    author = models.CharField(null=True, blank=True)
    date = models.CharField(null=True, blank=True)
    timestamp = models.CharField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(null=True, blank=True)
    post_type = models.CharField(null=True, blank=True, default='entity')
 
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