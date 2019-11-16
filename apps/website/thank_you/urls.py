from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.thank_you.views',

                       url(r'^thank_you/$', 'thank_you', name='thank_you'),

                       )