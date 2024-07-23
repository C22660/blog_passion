from django import forms
from django.utils.translation import gettext_lazy as _

# from crispy_forms.helper import FormHelper

from blog.articles.models import Article

class CreationArticleForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     print(args)
    #     super().__init__(*args, **kwargs)

    #     self.helper = FormHelper()
    #     self.helper.form_tag = False
    #     self.helper.layout = CreationActivityFormLayout()

    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "image",
            "published",
        ]
