from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', 'qa.views.test', name='home'),

    url(r'^', include('qa.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
