from django import forms

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
