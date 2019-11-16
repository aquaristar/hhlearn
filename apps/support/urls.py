from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView


urlpatterns = patterns('apps.support.views',
                        url(r'^support/$', 'index', name='support_home'),
                       )
