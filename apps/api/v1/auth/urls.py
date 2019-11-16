from django.conf.urls import patterns, include, url
from login import *
from signup import *
from reset import *

urlpatterns = patterns('',

                       (r'^api/v1/auth/login?$', APIAuthLogin.as_view()),

                       (r'^api/v1/auth/signup?$', APIAuthSignup.as_view()),

                       (r'^api/v1/auth/reset?$', APIAuthReset.as_view()),

                       (r'^api/v1/auth/reset/save?$', APIAuthReset.as_view()),

                       url(r'^api/v1/auth/token', 'rest_framework.authtoken.views.obtain_auth_token'),
)
