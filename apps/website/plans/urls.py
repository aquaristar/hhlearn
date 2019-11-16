from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.plans.views',

                       url(r'^plans/$', 'plans', name='plans'),

                       )