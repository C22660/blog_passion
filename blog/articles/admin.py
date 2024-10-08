from django.contrib import admin

# Register your models here.
from blog.articles.models import Article


@admin.register(Article)
class ArtcicleAdmin(admin.ModelAdmin):
    list_display = ('title',  'content',  'image', 'author', 'created_at',
                    'updated_at', 'published_on', 'published')
    list_editable = ('published',)
