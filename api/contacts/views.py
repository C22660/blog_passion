from rest_framework.response import Response
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

from api.contacts.serializers import ContactSerializer


@swagger_auto_schema(
    method='post',
    operation_description="Fill out the contact form",
    response={200: ContactSerializer}
    )
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
