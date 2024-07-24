from django.urls import path
from blog.events.views import events_view

app_name = "events"

urlpatterns = [
    path("events/", events_view, name="all-events"),
]