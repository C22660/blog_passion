from django.urls import path

from api.users.views import signup_view

app_name = 'api-users'

urlpatterns = [
    path('api/signup', signup_view, name="signup"),
]
