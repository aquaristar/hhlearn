from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.assignments.views',

                       url(r'^dashboard/assignments/$', 'assignments', name='assignments'),

                       )
