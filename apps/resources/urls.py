from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView


urlpatterns = patterns('apps.resources.views',
                        url(r'^resources/$', 'index', name='resources_home'),
                        url(r'^resources/files/(?P<code_encrypted>.+)?$', 'files', name='resources_files'),
                       )
