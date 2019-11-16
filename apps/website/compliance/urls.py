from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.compliance.views',

                       url(r'^compliance/$', 'compliance', name='compliance'),

                       )