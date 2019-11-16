from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
                       (r'^api/user/$', APIUser.as_view()),
                       (r'^api/users/$', APIUsers.as_view()),
                       (r'^api/user/add_edit/$', APIUserAddEdit.as_view()),
                       (r'^api/user/signup/zipcodes/$', APIUserZipCodes.as_view()),
                       )
