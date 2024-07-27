from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
 
from api.articles.views import ArticleViewset
 
# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé "article" et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/article/’
router.register('articles', ArticleViewset, basename='articles')
 
urlpatterns = [
    path('api/', include(router.urls))
]