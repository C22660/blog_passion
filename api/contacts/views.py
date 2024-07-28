from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.contacts.serializers import ContactSerializer


@api_view(['POST', ])
def contact_view(request):

    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            contact = serializer.save()
            data['response'] = 'Message envoyé avec succès'
            data['contact_email'] = contact.contact_email
            data['reason'] = contact.reason
            data['content'] = contact.content
        else:
            data = serializer.errors
        return Response(data)