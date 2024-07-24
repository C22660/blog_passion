from django.urls import path
from blog.articles.views import articles_view, creation_article_view, update_article_view, delete_article_view

app_name = "articles"

urlpatterns = [
    path("", articles_view, name="all-articles"),
    path("articles/creation/", creation_article_view, name="creation-article"),
    path(
        "articles/<slug:slug>/update/",
        update_article_view,
        name="article-detail-update",
    ),
    path(
        "articles/<slug:slug>/delete/",
        delete_article_view,
        name="article-detail-delete",
    ),
]