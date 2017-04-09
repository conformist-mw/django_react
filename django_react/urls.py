from django.conf.urls import include, url
from django.contrib import admin
from instant.views import index, register, get_user_profile

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/', register, name='register'),
    url(r'^accounts/(?P<username>.+)/$', get_user_profile),
    url(r'^instant/', include('instant.urls')),
    url(r'^sms/', include('sms.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('social_django.urls', namespace='social')),
    url(r'^(?:.*)/?$', index, name='index'),
]
