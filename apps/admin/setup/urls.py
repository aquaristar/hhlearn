from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.admin.setup.views',

                       url(r'^admin/setup/$', 'home', name='admin_setup'),
                       url(r'^admin/setup/complete$', 'complete', name='admin_setup_complete'),

                       (r'', include('apps.admin.setup.department.urls')),
                       (r'', include('apps.admin.setup.job_title.urls')),
                       (r'', include('apps.admin.setup.location.urls')),
                       (r'', include('apps.admin.setup.organization.urls')),
                       (r'', include('apps.admin.setup.region.urls')),

                       )
