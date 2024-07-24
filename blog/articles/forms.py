from django import forms
from django.utils.translation import gettext_lazy as _

# from crispy_forms.helper import FormHelper

from blog.articles.models import Article

class CreationArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "image",
            "published",
        ]
