from django.conf.urls import url, include
from django.contrib import admin
from . import settings
from django.views import(
    static
    )

urlpatterns = [
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('apps.users.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^publicacion/', include('apps.publi.urls')),
    
]
