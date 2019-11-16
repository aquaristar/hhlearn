from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.pricing.views',

                       url(r'^pricing/$', 'pricing', name='pricing'),

                       )