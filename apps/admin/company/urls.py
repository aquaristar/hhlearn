from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.admin.company.views',

                       url(r'^admin/company$', 'home', name='admin_company'),

                       (r'', include('apps.admin.company.locations.urls')),

                       )
