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

    def validate_title(self, value):
        '''Forbid title duplication for articles, but avoid
        PUT method to be catched.'''
        if not self.context['request'].method == 'PUT':
            if Article.objects.filter(title=value).exists():
                raise serializers.ValidationError('Article already exists')
        return value