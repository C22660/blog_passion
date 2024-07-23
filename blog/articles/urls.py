from django.urls import path
from blog.articles.views import articles_view

app_name = "articles"

urlpatterns = [
    path("", articles_view, name="all-articles"),
]