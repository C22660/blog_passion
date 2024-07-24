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

from blog.articles.models import Article
from blog.articles.forms import CreationArticleForm

# To create an article
class CreationArticleView(CreateView):
    model = Article
    template_name = "articles/create_article.html"
    form_class = CreationArticleForm
    success_url = reverse_lazy("articles:all-articles")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_part"] = _("Rédaction")
        context["submit_text"] = _("créer")
        return context

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            
        if form.cleaned_data.get("published"):
            form.instance.published_on = date.today()

        return super().form_valid(form)

creation_article_view = CreationArticleView.as_view()

# To display the articles.
class ArticleListView(ListView):
    model = Article
    context_object_name = "all_articles"
    ordering = ["published_on"]
    template_name = "articles/all_articles.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        else:
            return queryset.filter(published=True)

articles_view = ArticleListView.as_view()

# To update an article
class UpdateArticleView(UpdateView):
    model = Article
    template_name = "articles/create_article.html"
    form_class = CreationArticleForm
    success_url = reverse_lazy("articles:all-articles")

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


update_article_view = UpdateArticleView.as_view()

# To delete an article
class DeleteArticleView(DeleteView):
    model = Article
    template_name = "articles/confirmation_delete.html"
    context_object_name = "element"
    success_url = reverse_lazy("articles:all-articles")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_subject"] = "un article"
        context["question"] = (
            f"""Voulez-vous supprimer l'article "{ context["element"].title }" ? """
        )
        previous_page = self.request.META.get("HTTP_REFERER", "/")
        context["previous_page"] = previous_page
        return context


delete_article_view = DeleteArticleView.as_view()