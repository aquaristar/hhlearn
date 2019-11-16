from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.documents.views',

                       url(r'^dashboard/documents/$', 'documents', name='documents'),

                       )
