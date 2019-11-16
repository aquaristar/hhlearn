from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.admin.setup.region.views',

		       url(r'^admin/setup/region_4$', 'region_4', name='admin_setup_region_4'),


		       url(r'^admin/setup/region_4_1$', 'region_4_1', name='admin_setup_region_4_1'),

		       url(r'^admin/setup/region_4_1/(?P<region_number>\d+)/$', 'region_4_1', name='admin_setup_region_4_1_questions'),


		       )
