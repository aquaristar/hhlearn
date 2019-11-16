from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.reporting.views',

                       url(r'^reporting/$', 'reporting', name='reporting'),

                       )