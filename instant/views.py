from rest_framework.viewsets import ModelViewSet
# from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import User
from .serializers import UserSerializer


class UserPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # renderer_classes = [JSONRenderer]
    permission_class = DjangoModelPermissionsOrAnonReadOnly
    pagination_class = UserPagination
