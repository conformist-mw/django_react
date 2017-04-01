from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User as UserProfile
from .models import User
from .serializers import UserSerializer, BaseUserSerializer
from .forms import UserCreateForm


class UserPagination(PageNumberPagination):
    page_size = 20
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


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    args = {}
    args['form'] = UserCreateForm()
    return render(request, 'registration/register.html', args)


def support(request):
    return render(request, 'instant/support.html')


def get_user_profile(request, username):
    user = UserProfile.objects.get(username=username)
    return render(request, 'registration/profile.html', {'user': user})
