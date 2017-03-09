from rest_framework import viewsets, renderers
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [renderers.JSONRenderer]


class UserDetail(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    renderer_classes = [renderers.JSONRenderer]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return User.objects.filter(pk=pk)
