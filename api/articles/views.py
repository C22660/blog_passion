from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
 
from blog.articles.models import Article
from api.articles.serializers import ArticleDetailSerializer
from api.articles.permissions import ArticleAdministrationPermissions

class ArticleViewsetForVisitor(ReadOnlyModelViewSet):
 
    serializer_class = ArticleDetailSerializer

    @swagger_auto_schema(
        operation_description="Display the detail of an article ", 
        responses={200: 'ArticleDetailSerializer'}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(
            request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Display the list of articles",
        responses={200: 'ArticleDetailSerializer'}
        )
    def list(self):
        return super().list(self)

 
    def get_queryset(self):
        return Article.objects.filter(published=True)


class ArticleViewset(ModelViewSet):
 
    serializer_class = ArticleDetailSerializer
    filterset_fields = ['published']
    permission_classes = [IsAuthenticated, ArticleAdministrationPermissions]

    @swagger_auto_schema(
        operation_description="Display the list of articles",
        responses={200: 'ArticleDetailSerializer'}
        )
    def list(self):
        return super().list(self)

    def get_queryset(self):
        return Article.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @swagger_auto_schema(
        operation_description="Display the detail of an article ", 
        responses={200: 'ArticleDetailSerializer'}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(
            request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create an article ", 
        responses={200: 'ArticleDetailSerializer'}
    )
    def create(self, request, *args, **kwargs):
        return super().create(
            request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Destroy an article ", 
        responses={200: 'ArticleDetailSerializer'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(
            request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Modify an article ", 
        responses={200: 'ArticleDetailSerializer'}
    )
    def update(self, request, *args, **kwargs):
        return super().update(
            request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partial modification of an article ", 
        responses={200: 'ArticleDetailSerializer'}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(
            request, *args, **kwargs)