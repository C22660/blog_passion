from django.urls import path

from blog.contacts.views import send_contact_message

app_name = "contacts"

urlpatterns = [
    path("contacts/message/", send_contact_message, name="contact-message"),
]