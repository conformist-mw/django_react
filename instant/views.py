from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import User
from .serializers import UserSerializer, BaseUserSerializer


class UserPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    renderer_classes = [JSONRenderer]
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = UserPagination

    def get_serializer_class(self):
        if not self.request.user.is_anonymous:
            return UserSerializer
        return BaseUserSerializer


def index(request):
    return render(request, 'instant/index.html')
