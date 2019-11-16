from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.demos.views',

                       url(r'^demos/$', 'demos', name='demos'),

                       )