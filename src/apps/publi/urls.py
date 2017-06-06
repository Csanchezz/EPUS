from django.conf.urls import url
from apps.publi.views import *

urlpatterns = [
    url(r'^crear/$', CreatePost.as_view(), name='create_post'),
    url(r'^add/$', ViewPost.as_view(), name='view_private_post'),
    url(r'^add/editar/(?P<post_pk>\d+)/$', EditPost.as_view(), name='edit_post'),
    url(r'^$', publico, name='view_post'),
    url(r'^error/', error, name='error_post'),
  
]
