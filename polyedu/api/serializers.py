from rest_framework import serializers
from ..models import Article

class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('user', 'title', 'desc', 'body', 'created_at', 'likes', 'category')