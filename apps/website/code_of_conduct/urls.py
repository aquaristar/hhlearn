from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.code_of_conduct.views',

                       url(r'^code_of_conduct/$', 'code_of_conduct', name='code_of_conduct'),

                       )