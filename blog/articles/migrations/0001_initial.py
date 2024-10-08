# Generated by Django 5.0.7 on 2024-07-22 13:44

import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Articles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200,
                                           verbose_name="titre")),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        populate_from=["title"],
                        unique=True,
                        verbose_name="article slug",
                    ),
                ),
                ("content", models.TextField(blank=True,
                                             verbose_name="contenu")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="article/images/activity",
                        verbose_name="Image de l'article",
                    ),
                ),
                ("published_on", models.DateField(blank=True, null=True)),
                (
                    "published",
                    models.BooleanField(default=False, verbose_name="publié"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "articles",
                "ordering": ["-published_on"],
            },
        ),
    ]
