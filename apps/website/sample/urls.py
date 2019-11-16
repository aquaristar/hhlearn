from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.sample.views',

                       url(r'^sample/$', 'sample', name='sample'),

                       )