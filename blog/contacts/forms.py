from django import forms
from django.utils.translation import gettext_lazy as _


from blog.contacts.models import Contact

class CreationContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            "contact_email",
            "reason",
            "content",
        ]