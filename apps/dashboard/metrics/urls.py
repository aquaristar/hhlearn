from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.metrics.views',

                       url(r'^dashboard/metrics/$', 'metrics', name='metrics'),

                       )
