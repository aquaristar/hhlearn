from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.courses.views',

                       # URL must have the encypted course code.
                       url(r'^dashboard/course/(?P<course_code_encrypted>.+)?$', 'course', name='dashboard_course'),
                       url(r'^dashboard/course/pdf/(?P<course_code_encrypted>.+)?$', 'print_pdf', name='dashboard_course_pdf'),

                       )
