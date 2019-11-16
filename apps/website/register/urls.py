from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.register.views',

                       #registration page
                       url(r'register$', 'register', name='register'),

                       #thank you page after registration
                       url(r'successful$', 'register_successful', name='register_successful'),

                       )
