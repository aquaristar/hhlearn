from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView


urlpatterns = patterns('apps.inservices.views',
                        url(r'^inservices/$', 'index', name='inservices_home'),
                       )
