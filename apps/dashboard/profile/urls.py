from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.profile.views',

                       # dashboard url. which is root "/"
                       url(r'^dashboard/profile/$', 'home', name='profile_home'),
                       url(r'^dashboard/profile/view', 'view', name='profile_view'),                       

                       )
