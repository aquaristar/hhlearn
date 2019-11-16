from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.contact.views',

                       url(r'^contact/$', 'contact', name='contact'),

                       )