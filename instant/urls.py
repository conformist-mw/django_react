from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, support

router = routers.DefaultRouter()
router.register(r'api', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^support/', support, name='support'),
]
