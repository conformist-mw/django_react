from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User as UserProfile
from .models import User
from .serializers import UserSerializer, BaseUserSerializer
from .forms import UserCreateForm, FeedBack
from django.core.mail import send_mail


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
    if request.method == 'POST':
        form = FeedBack(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['first_name']
            surname = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message = message + \
                '\nFrom {} {}. Phone: {}'.format(name, surname, phone)
            recipient = ['conformist.mw@gmail.com']
            send_mail(subject, message, email, recipient)
            return redirect('/')
    else:
        if request.user.is_authenticated():
            form = FeedBack(initial={'first_name': request.user.first_name,
                                     'last_name': request.user.last_name,
                                     'email': request.user.email})
            form.fields['first_name'].widget.attrs['disabled'] = True
            form.fields['last_name'].widget.attrs['disabled'] = True
            form.fields['email'].widget.attrs['disabled'] = True
        else:
            form = FeedBack()
    return render(request, 'instant/support.html', {'form': form})


def get_user_profile(request, username):
    user = UserProfile.objects.get(username=username)
    return render(request, 'registration/profile.html', {'user': user})
