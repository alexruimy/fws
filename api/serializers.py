from articles.models import Article
from rest_framework import serializers

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'body', 'author')