from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from blog.events.models import Event


class EventDetailSerializer(ModelSerializer):
    """Serializer for the event model wich display the list of events
    with all elements."""

    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Event
        # Normalement tous les champs par défaut, mais ajout de _all_ pour
        # être explicite.
        fields = '__all__'
        # Contraierement aux articles,
        # ici, on permet les évènements de même nom (ex sortie théatre)
