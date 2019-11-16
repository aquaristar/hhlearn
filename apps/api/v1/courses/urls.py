from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
                       (r'^api/courses/$', APICourses.as_view()),
                       (r'^api/course/start/$', APICourseStart.as_view()),
                       (r'^api/assignment_courses_list/', APIAssignmentCoursesList.as_view()),
                       )
