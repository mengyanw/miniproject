from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from ..models import Post

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
