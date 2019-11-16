from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.courses.views',

                       url(r'^courses/$', 'courses', name='courses'),

                       )