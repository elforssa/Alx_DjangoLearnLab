from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

from rest_framework.authtoken.models import Token
, "serializers.CharField()", "Token.objects.create", "get_user_model().objects.create_user"