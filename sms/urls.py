from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.KeyViewSet.as_view({'get': 'create'})),
    url(r'^last/$', views.KeyViewSet.as_view({'get': 'last'})),
    url(r'^check/(?P<key>[a-zA-Z0-9]{4})/$', views.KeyViewSet.as_view({'get': 'retrieve'})),
    url(r'^submit/(?P<key>[a-zA-Z0-9]{4})/$', views.KeyViewSet.as_view({'get': 'submit'})),
    url(r'^$', views.index),
]
