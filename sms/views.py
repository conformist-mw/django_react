from random import choice
from string import ascii_letters, digits
from .models import Key
from .serializers import KeySerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404, render


class KeyViewSet(ViewSet):
    renderer_classes = [JSONRenderer]

    def create(self, request):
        while True:
            key = ''.join(choice(ascii_letters + digits) for _ in range(4))
            if not Key.objects.filter(id=key).exists():
                break
        new_key = Key(id=key)
        new_key.save()
        serializer = KeySerializer(new_key)
        return Response(serializer.data)

    def retrieve(self, request, key):
        query_key = get_object_or_404(Key.objects.filter(id=key))
        serializer = KeySerializer(query_key)
        return Response(serializer.data)

    def submit(self, request, key):
        query_key = get_object_or_404(Key.objects.filter(id=key))
        if query_key:
            query_key.active = False
            query_key.save()
        serializer = KeySerializer(query_key)
        return Response(serializer.data)

    def last(self, request):
        possible_keys = 677040
        all_keys = Key.objects.count()
        return Response({'last': possible_keys - all_keys})


def index(request):
    return render(request, 'sms/index.html')
