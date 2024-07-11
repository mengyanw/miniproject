from ...models import Post
import requests
import os
from dotenv import load_dotenv
load_dotenv()

from transformers import pipeline
# sentiment_pipeline = pipeline("sentiment-analysis")
sentiment_pipeline = pipeline('sentiment-analysis', model="cardiffnlp/twitter-roberta-base-sentiment-latest")

def get_data(cursor, post_type):
    params = {'entity': 'basketball_4', 'start_date':'2024-05-01', 'media':'twitter', 'order': 'engagement', 'post_type': post_type, 'limit': '100'}
    if cursor:
        params['cursor'] = cursor

    response = requests.get(os.getenv("API"), params=params, headers={'authorization': 'Bearer ' + os.getenv("TOKEN")})
    data = response.json()
    print(len(data['posts']))
        
    for each in data['posts']:
        sentiment = sentiment_pipeline(each['original_description'])
        post = Post.objects.create(
            author = each['author'],
            date = each['date'],
            timestamp = each['timestamp'],
            description = each['original_description'],
            url = each['url'],
            medium_id = each['medium_id'],
            
            engagement = each['engagement'],
            public_impressions = each['public_impressions'],
            estimated_views = each['estimated_views'],
            liked_count = each['liked_count'],
            replied_count = each['replied_count'],
            reposted_count = each['reposted_count'],
            post_type=post_type,
            
            sentiment_label = sentiment[0]['label'],
            sentiment_score = sentiment[0]['score'],
        )
        post.save()
    
    if 'next_page' in data:
        print('next_page')
        get_data(data['next_page'], post_type)
