from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from blog.articles.models import Article


class ArticleDetailSerializer(ModelSerializer):
    """Serializer for the Article model wich display the list of articles
    with all elements."""

    class Meta:
        model = Article
        # Normalement tous les champs par défaut, mais ajout de _all_ pour
        # être explicite.
        fields = '__all__'

    # def validate_title(self, value):
    #     if Article.objects.filter(title=value).exists():
    #         if not self.request.method == 'PUT':
    #             raise serializers.ValidationError('Article already exists')
    #     return value