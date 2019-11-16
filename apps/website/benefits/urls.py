from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.benefits.views',

                       url(r'^benefits/$', 'benefits', name='benefits'),

                       )
