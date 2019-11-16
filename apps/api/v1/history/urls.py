from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',                       
                       (r'^api/history/test/$', APITestHistory.as_view()),
                       (r'^api/history/testattempt/$', APITestAttempt.as_view()),
                       )
