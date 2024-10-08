from django.contrib import admin

# Register your models here.
from blog.contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_email', 'reason', 'content',  'created_at')
