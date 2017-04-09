from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User as UserProfile
from .models import User
from .serializers import UserSerializer, BaseUserSerializer
from .forms import UserCreateForm, FeedBack
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login


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


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/')
    else:
        form = UserCreateForm()
    return render(request, 'registration/register.html', {'form': form})


def support(request):
    if request.method == 'POST':
        form = FeedBack(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['first_name']
            surname = form.cleaned_data['last_name']
            email_from = form.cleaned_data['email']
            email_from = '{} {} <{}>'.format(name, surname, email_from)
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = ['conformist.mw@gmail.com']
            email = EmailMessage(subject, message, email_from, recipient)
            email.attach(form.cleaned_data['image'].name,
                         form.cleaned_data['image'].read(),
                         form.cleaned_data['image'].content_type)
            email.send()
            return render(request, 'instant/success.html')
    else:
        if request.user.is_authenticated():
            form = FeedBack(initial={'first_name': request.user.first_name,
                                     'last_name': request.user.last_name,
                                     })
            form.fields['first_name'].widget.attrs['disabled'] = True
            form.fields['last_name'].widget.attrs['disabled'] = True
        else:
            form = FeedBack()
    return render(request, 'instant/support.html', {'form': form})


def get_user_profile(request, username):
    user = UserProfile.objects.get(username=username)
    return render(request, 'registration/profile.html', {'user': user})
