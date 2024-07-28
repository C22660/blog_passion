from django.db import models
from django.conf import settings
from django_extensions.db.fields import AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


from PIL import Image

class Event(models.Model):
    """Each event will be registered here.
    """

    title = models.CharField(_("titre"), max_length=200)
    slug = AutoSlugField(
        "event slug",
        populate_from=["title"],
        unique=True,
    )
    content = models.TextField(_("description"), blank=True)
    image = models.ImageField(
        _("Image de l'événement"),
        upload_to="event/images/events",
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="events",
        verbose_name=_("auteur"),
    )
    date_begin = models.DateField(
        _("date de début"),
        blank=True,
        null=True,
    )
    date_finish = models.DateField(
        _("date de fin"),
        blank=True,
        null=True,
    )
    published_on = models.DateField(_("publié le"),blank=True, null=True)
    published = models.BooleanField(_("publié"), default= False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    IMAGE_MAX_SIZE = (400, 150)

    class Meta:
        verbose_name_plural = _("événements")
        ordering = ['-published_on']

    def __str__(self):
        return self.title

    # Adaptation du format de l'image à un max définit en IMAGE_MAX_SIZE
    # A placer dans le formulaire
    def resize_image(self):
        with Image.open(self.image) as image:
            image.thumbnail(self.IMAGE_MAX_SIZE)
            image.save(self.image.path)
