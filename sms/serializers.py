from rest_framework import serializers
from .models import Key


class KeySerializer(serializers.ModelSerializer):

    class Meta:
        model = Key
        fields = ['id', 'active']
