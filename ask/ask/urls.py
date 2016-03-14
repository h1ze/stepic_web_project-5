from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^', include('qa.urls'))  - other way - in another file
    
    url(r'^$', 'qa.views.questions', name='questions'),
    url(r'^login/.*$', 'qa.views.test', name='login'),
    url(r'^signup/.*$', 'qa.views.test', name='signup'),
    url(r'^question/(?P<id>\d+)/$', 'qa.views.question_details', name='question_details'),
    url(r'^ask/.*$', 'qa.views.test', name='ask'),
    url(r'^popular/$', 'qa.views.popular_questions', name='popular_questions'),
    url(r'^new/.*$', 'qa.views.test', name='new'),
)

