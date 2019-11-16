from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.admin.company.locations.views',

                       url(r'^admin/company/locations$', 'home', name='admin_company_locations'),

                       )
