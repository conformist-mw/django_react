from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('full_name', 'age', 'birth', 'email', 'ipv4', 'phone', 'street', 'city')
