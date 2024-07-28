from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
 
from blog.events.models import Event
from api.events.serializers import EventDetailSerializer
from api.events.permissions import EventAdministrationPermissions

class EventViewsetForVisitor(ReadOnlyModelViewSet):
 
    serializer_class = EventDetailSerializer
 
    def get_queryset(self):
        return Event.objects.filter(published=True)


class EventViewset(ModelViewSet):
 
    serializer_class = EventDetailSerializer
    filterset_fields = ['published']
    permission_classes = [IsAuthenticated, EventAdministrationPermissions]
 
    def get_queryset(self):
        return Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
