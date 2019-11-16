from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.auth.views',

                       url(r'^login/$', 'auth_login', name='dashboard_login'),

                       url(r'^logout/$', 'auth_logout', name='dashboard_logout'),

                       )
