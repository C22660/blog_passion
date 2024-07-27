from rest_framework.viewsets import ModelViewSet
 
from blog.articles.models import Article
from api.articles.serializers import ArticleDetailSerializer
 
class ArticleViewset(ModelViewSet):
 
    serializer_class = ArticleDetailSerializer
    filterset_fields = ['published']
 
    def get_queryset(self):
        return Article.objects.all()