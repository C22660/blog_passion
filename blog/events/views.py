from datetime import date

from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog.events.models import Event



# To display the articles.
class EventListView(ListView):
    model = Event
    context_object_name = "all_events"
    ordering = ["published_on"]
    template_name = "events/all_events.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        else:
            return queryset.filter(published=True)

events_view = EventListView.as_view()