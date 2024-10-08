from django import forms

from blog.contacts.models import Contact


class CreationContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            "contact_email",
            "reason",
            "content",
        ]
