from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.messages.views',

                       url(r'^dashboard/messages/$', 'messages', name='messages'),

                       )
