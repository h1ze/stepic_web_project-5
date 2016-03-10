from django.conf.urls import patterns, include, url
from qa.views import test

urlpatterns = patterns('qa.views',
    url(r'^$', test, name='homepage'),
    url(r'^login/$', test, name='login'),
    url(r'^signup/$', test, name='signup'),
    url(r'^question/(\d+)/$', test, name='question'),
    url(r'^ask/$', test, name='ask'),
    url(r'^ask//popular/$', test, name='popular'),
    url(r'^new/$', test, name='new'),
)
