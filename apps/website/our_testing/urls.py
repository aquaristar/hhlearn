from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.our_testing.views',

                       url(r'^our_testing/$', 'our_testing', name='our_testing'),

                       )