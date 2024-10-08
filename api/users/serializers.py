from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserSerializer(ModelSerializer):
    """Serialize User class for user creation"""
    password2 = serializers.CharField(style={'input_type': 'password'},
                                      write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
                        'password': {'write_only': True}
                       }

    # pour s'assurer que password et passorwd2 matchent, on overwrite
    # la méthode save
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':
                                               """Les mots de passe
                                               doivent être
                                               identiques"""}
                                              )

        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user
