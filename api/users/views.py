from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

from drf_yasg.utils import swagger_auto_schema

from api.users.serializers import UserSerializer


@swagger_auto_schema(
    method='post',
    operation_description="Create a user (limited access)",
    response={200: UserSerializer}
    )
@api_view(['POST', ])
@permission_classes([IsAdminUser])
def signup_view(request):

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Nouvel utilisateur enregistré avec succès'
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)
