# Generated by Django 5.0.7 on 2024-07-22 16:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0003_rename_articles_article"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="articles",
                to=settings.AUTH_USER_MODEL,
                verbose_name="auteur",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="published_on",
            field=models.DateField(blank=True, null=True,
                                   verbose_name="publié le"),
        ),
    ]
