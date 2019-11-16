from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.alerts.views',

                       url(r'^dashboard/alerts$', 'index', name='alerts_home'),

                       )
