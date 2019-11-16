from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.testimonials.views',

                       url(r'^testimonials/$', 'testimonials', name='testimonials'),

                       )