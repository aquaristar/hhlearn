from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.login.views',

                       url(r'^login/$', 'login', name='login'),

                       )