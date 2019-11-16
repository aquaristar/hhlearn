from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.choose_edition.views',

                       url(r'^choose_edition/$', 'choose_edition', name='choose_edition'),

                       )