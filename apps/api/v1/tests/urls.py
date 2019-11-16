from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
                       (r'^api/tests/$', APITestAttempt.as_view()),
                       (r'^api/test/start/$', APITestStart.as_view()),                       
                       (r'^api/test/end/$', APITestEnd.as_view()),                       
                       (r'^api/test/result/$', APITestResult.as_view()),
                       (r'^api/tests/all/$', APITestAll.as_view()),
                       (r'^api/test/add_edit/$', APITestAdd.as_view()),
                       (r'^api/test/question/$', APITestQuestion.as_view()),
                       (r'^api/test/question/county_fips/$', APICountyFips.as_view()),
                       )
