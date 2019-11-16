from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.privacy.views',

                       url(r'^privacy/$', 'privacy', name='privacy'),

                       )