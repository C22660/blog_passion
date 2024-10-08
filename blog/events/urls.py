from django.urls import path
from blog.events.views import (events_view, creation_event_view,
                               update_event_view, delete_event_view)

app_name = "events"

urlpatterns = [
    path("events/", events_view, name="all-events"),
    path("events/creation/",
         creation_event_view,
         name="creation-event",
         ),
    path(
        "events/<slug:slug>/update/",
        update_event_view,
        name="event-detail-update",
        ),
    path(
        "events/<slug:slug>/delete/",
        delete_event_view,
        name="event-detail-delete",
        ),
]
