from django.conf.urls import url
from .views import UserViewSet, UserDetail

urlpatterns = [
    url(r'^users/$', UserViewSet.as_view({'get': 'list'}), name='users-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view({'get': 'retrieve'}), name='users-detail'),
]
