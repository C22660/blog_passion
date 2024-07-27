from rest_framework.viewsets import ModelViewSet
 
from blog.articles.models import Article
from api.articles.serializers import ArticleDetailSerializer
 
class ArticleViewset(ModelViewSet):
 
    serializer_class = ArticleDetailSerializer
 
    def get_queryset(self):
        return Article.objects.all()

    # Pour pouvoir faire un update partiel
    # https://tech.serhatteker.com/post/2020-09/enable-partial-update-drf/
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
