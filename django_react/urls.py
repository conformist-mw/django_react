from django.conf.urls import include, url
from django.contrib import admin
from instant.views import index

urlpatterns = [
    url(r'^instant/', include('instant.urls')),
    url(r'^sms/', include('sms.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', index, name='index'),
]
