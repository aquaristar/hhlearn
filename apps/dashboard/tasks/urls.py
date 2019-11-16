from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.tasks.views',

                       # URL must have the encypted course code.
                       url(r'^dashboard/tasks/$', 'index', name='dashboard_tasks'),

                       )
