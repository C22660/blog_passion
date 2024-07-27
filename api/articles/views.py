from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
 
from blog.articles.models import Article
from api.articles.serializers import ArticleDetailSerializer
from api.articles.permissions import ArticleAdministrationPermissions

class ArticleViewsetForVisitor(ReadOnlyModelViewSet):
 
    serializer_class = ArticleDetailSerializer
 
    def get_queryset(self):
        return Article.objects.filter(published=True)


class ArticleViewset(ModelViewSet):
 
    serializer_class = ArticleDetailSerializer
    filterset_fields = ['published']
    permission_classes = [IsAuthenticated, ArticleAdministrationPermissions]
 
    def get_queryset(self):
        return Article.objects.all()