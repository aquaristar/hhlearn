from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',

                       # URL for GET our profile page.
                       # this same user will be used with various actions like GET, POST, PUT, DELETE
                       (r'^api/v1/assignments?$', Assignments.as_view()),
                       (r'^api/v1/assignment/(?P<pk>[0-9]+)$', AssignmentDetail.as_view()),
)
