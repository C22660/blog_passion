from django import forms

from blog.events.models import Event


class CreationEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = [
            "title",
            "content",
            "image",
            "date_begin",
            "date_finish",
            "published",
        ]
