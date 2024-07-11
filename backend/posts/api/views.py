from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from ..models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Avg, Count, DateTimeField
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth, Cast


def time_series_analysis(posts, trunc_by='day'):
    formatted_posts = posts.annotate(
        created_at_datetime=Cast(
            'date',
            output_field=DateTimeField()
        )
    )
    aggregated_engagement = []
    if trunc_by == 'day':
        aggregated_engagement = formatted_posts.annotate(day=TruncDay('created_at_datetime')).values(trunc_by, 'sentiment_label').annotate(
            avg_engagement=Avg('engagement'),
            post_count=Count('medium_id')
        ).order_by('day')
    elif trunc_by == 'week':
        aggregated_engagement = formatted_posts.annotate(week=TruncWeek('created_at_datetime')).values(trunc_by, 'sentiment_label').annotate(
            avg_engagement=Avg('engagement'),
            post_count=Count('medium_id'),
        ).order_by('week')
    elif trunc_by == 'month':
        aggregated_engagement = formatted_posts.annotate(month=TruncMonth('created_at_datetime')).values(trunc_by, 'sentiment_label').annotate(
            avg_engagement=Avg('engagement'),
            post_count=Count('medium_id')
        ).order_by('month')
    
    transformed_data = {}
    for entry in aggregated_engagement:
        sentiment_label = entry['sentiment_label']
        data_point = {
            "x": entry[trunc_by],
            "y": entry['avg_engagement'],
        }
        if sentiment_label not in transformed_data:
            transformed_data[sentiment_label] = []
        transformed_data[sentiment_label].append(data_point)

    result = [
        {
            "name": sentiment_label,
            "data": data_points
        }
        for sentiment_label, data_points in transformed_data.items()
    ]    
    return result

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['get'])
    def time_series(self, request):
        posts = Post.objects.all()
        trunc_by = request.query_params.get('trunc_by', 'day')
        analysis_result = time_series_analysis(posts, trunc_by)
        return JsonResponse(analysis_result, safe=False)

    @action(detail=False, methods=['get'])
    def topN(self, request):
        neg_posts = Post.objects.filter(sentiment_label="negative").order_by("-engagement")[:3]
        neu_posts = Post.objects.filter(sentiment_label="neutral").order_by("-engagement")[:3]
        pos_posts = Post.objects.filter(sentiment_label="positive").order_by("-engagement")[:3]

        transformed_data = {}
        for entry in list(neg_posts) + list(neu_posts) + list(pos_posts):
            sentiment_label = entry.sentiment_label
            data = {
                "medium_id": entry.medium_id,
                "date": entry.date,
                "engagement": entry.engagement,
                "description": entry.description
            }
            if sentiment_label not in transformed_data:
                transformed_data[sentiment_label] = []
            transformed_data[sentiment_label].append(data)
        
        return JsonResponse(transformed_data, safe=False)