from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.our_modules.views',

                       url(r'^our_modules/$', 'our_modules', name='our_modules'),

                       )