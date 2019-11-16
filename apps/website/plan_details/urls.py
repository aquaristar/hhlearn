from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.plan_details.views',

                       url(r'^plan_details/$', 'plan_details', name='plan_details'),

                       )