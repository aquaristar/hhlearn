from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.admin.views',

                       url(r'^admin/$', 'home', name='admin_home'),                       

                       (r'', include('apps.admin.company.urls')),
                       (r'', include('apps.admin.setup.urls')),
                       (r'', include('apps.admin.users.urls')),
                       (r'', include('apps.admin.tests.urls')),
                       )
