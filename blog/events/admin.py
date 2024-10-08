from django.contrib import admin

# Register your models here.
from blog.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title',  'content',  'image', 'author', 'date_begin',
                    'date_finish', 'created_at', 'updated_at', 'published_on',
                    'published')
    list_editable = ('published',)
