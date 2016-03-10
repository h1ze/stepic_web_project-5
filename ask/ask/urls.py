# ask URL Configuration

"""
from django.conf.urls import url
from stepic_web.ask.qa import views

urlpatterns =(\
  url("^$", views.get_questions, name="first_page", kwargs={"question_type": "new"}),
  url("^login/$",  views.test, name="login"),
  url("^signup/$",  views.test, name="signup"),
  url("^question/(?P<pk>\d+)/$",  views.test, name="question"),
  url("^ask/",  views.test, name="ask"),
  url("^popular/$",  views.get_questions, name="popular", kwargs={"question_type": "popular"}),
  url("^new/$",  views.get_questions, name="new", kwargs={"question_type": "new"})
)
"""
from django.conf.urls import url, patterns
from qa.views import test

urlpatterns = patterns('',
   url(r'^$', test, name='test'),
   url(r'^login/', test, name='login'),
   url(r'^signup/', test, name='signup'),
   url(r'^question/\d+/', test, name='question'),
   url(r'^ask/', test, name='aks'),
   url(r'^popular/', test, name='popular'),
   url(r'^new/', test, name='new'),
)