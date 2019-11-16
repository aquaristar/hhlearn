from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.home.views',

                       url(r'^dashboard/$', 'index', name='dashboard_home'),

                       )
