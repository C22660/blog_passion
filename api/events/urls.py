from django.urls import path, include
from rest_framework import routers

from api.events.views import EventViewset, EventViewsetForVisitor

# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé "event" et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/event/’
router.register('events_admin', EventViewset, basename='events_admin')
router.register('events', EventViewsetForVisitor, basename='events')

urlpatterns = [
    path('api/', include(router.urls))
]
