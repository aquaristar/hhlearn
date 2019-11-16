from django.conf.urls import patterns, include, url
from profile import *
from nav import *

urlpatterns = patterns('',

                       # URL for GET our profile page.
                       # this same user will be used with various actions like GET, POST, PUT, DELETE
                       (r'^api/v1/profile?$', APIProfile.as_view()),
                        (r'^api/v1/profile/min?$', APIProfileMin.as_view()),
                       (r'^api/v1/toggle_menu?$', APIToggelMenu.as_view()),
)
