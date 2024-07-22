from django.contrib import admin

# Register your models here.
from blog.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass