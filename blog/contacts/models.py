from datetime import datetime

from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext_lazy as _


def slugify_with_date(self):
    """AutoSlugField can't be populated by created_at when contact is saved.
    We use here datetime.now().
    """
    return "{}-{}".format(self.contact_email, datetime.now())


class Contact(models.Model):
    """A model for the contact message is not mandatory. But here, we could
    record all messages in the database for analysis purpose.
    """

    CHOICES = (
        ('CONTACT', 'Contact'),
        ('BUG', 'Remontée de bug'),
    )

    contact_email = models.EmailField(_("E-mail"))
    slug = AutoSlugField(
        "contact slug",
        populate_from=slugify_with_date,
        unique=True,
    )
    content = models.TextField(_("message"), blank=False)
    reason = models.CharField(_("motif"), max_length=15, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = _("contacts")

    def __str__(self):
        return f"{self.contact_email} ({self.created_at.day})"
