from django.shortcuts import render

from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog.articles.models import Article

# To display the articles.
class ArticleListView(ListView):
    model = Article
    context_object_name = "all_articles"
    ordering = ["published_on"]
    template_name = "articles/all_articles.html"

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     url_website = self.request.build_absolute_uri("/order/")
    #     context["url_website"] = url_website

    #     return context


articles_view = ArticleListView.as_view()