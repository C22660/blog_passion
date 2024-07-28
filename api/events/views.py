from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
 
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

    @swagger_auto_schema(
        operation_description="Display the list of articles",
        responses={200: 'ArticleDetailSerializer'}
        )
    def list(self):
        return super().list(self)

    @swagger_auto_schema(
        operation_description="Display the detail of an event ", 
        responses={200: 'EventDetailSerializer'}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(
            request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create an event ", 
        responses={200: 'EventDetailSerializer'}
    )
    def create(self, request, *args, **kwargs):
        return super().create(
            request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Destroy an event ", 
        responses={200: 'EventDetailSerializer'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(
            request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Modify an event ", 
        responses={200: 'EventDetailSerializer'}
    )
    def update(self, request, *args, **kwargs):
        return super().update(
            request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partial modification of an event ", 
        responses={200: 'EventDetailSerializer'}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(
            request, *args, **kwargs)
