from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.newsletter.views',

                       url(r'^newsletter/$', 'newsletter', name='newsletter'),

                       )