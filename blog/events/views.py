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
from blog.events.forms import CreationEventForm

# To create an article
class CreationEventView(CreateView):
    model = Event
    template_name = "events/create_event.html"
    form_class = CreationEventForm
    success_url = reverse_lazy("events:all-events")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_part"] = _("Création")
        context["submit_text"] = _("créer")
        return context

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            
        if form.cleaned_data.get("published"):
            form.instance.published_on = date.today()

        return super().form_valid(form)

creation_event_view = CreationEventView.as_view()


# To display the events.
class EventListView(ListView):
    model = Event
    context_object_name = "all_events"
    template_name = "events/all_events.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        else:
            return queryset.filter(published=True)

events_view = EventListView.as_view()

# To update an event
class UpdateEventView(UpdateView):
    model = Event
    template_name = "events/create_event.html"
    form_class = CreationEventForm
    success_url = reverse_lazy("events:all-events")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_part"] = _("Modification")
        context["submit_text"] = _("modifier")
        return context

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            
        if form.cleaned_data.get("published"):
            form.instance.published_on = date.today()
        else:
            form.instance.published_on = None

        return super().form_valid(form)


update_event_view = UpdateEventView.as_view()

# To delete an event
class DeleteEventView(DeleteView):
    model = Event
    template_name = "events/confirmation_delete.html"
    context_object_name = "element"
    success_url = reverse_lazy("events:all-events")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_subject"] = "un événement"
        context["question"] = (
            f"""Voulez-vous supprimer l'événement "{ context["element"].title }" ? """
        )
        previous_page = self.request.META.get("HTTP_REFERER", "/")
        context["previous_page"] = previous_page
        return context


delete_event_view = DeleteEventView.as_view()