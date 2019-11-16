from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.news.views',

                       url(r'^news/$', 'news', name='benefits'),

                       )