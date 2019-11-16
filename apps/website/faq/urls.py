from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.faq.views',

                       url(r'^faq/$', 'faq', name='faq'),

                       )