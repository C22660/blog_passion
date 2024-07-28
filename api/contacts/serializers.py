from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from blog.contacts.models import Contact


class ContactSerializer(ModelSerializer):
    """Serializer for the Contact form model."""

    class Meta:
        model = Contact
        fields = ['contact_email', 'content', 'reason']