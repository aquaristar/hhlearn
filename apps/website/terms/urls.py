from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.terms.views',

                       url(r'^terms/$', 'terms', name='terms'),

                       )