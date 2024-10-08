from django.urls import path

from api.contacts.views import contact_view

app_name = 'api-contact'

urlpatterns = [
    path('api/contact', contact_view, name="contact"),
]
