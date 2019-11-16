from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.history.views',

                       url(r'^dashboard/history/$', 'history', name='history'),

                       )
