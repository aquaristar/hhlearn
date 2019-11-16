from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.admin.setup.location.views',

                       url(r'^admin/setup/location_2_1$', 'location_2_1', name='admin_setup_location_2_1'),

                       #url(r'^admin/setup/location_2_1/(?P<question_start>\d+)/(?P<question_end>\d+)/$', 'location_2_1', name='admin_setup_location_2_1_questions'),

                       url(r'^admin/setup/location_2_2$', 'location_2_2', name='admin_setup_location_2_2'),

                       url(r'^admin/setup/location_2_3$', 'location_2_3', name='admin_setup_location_2_3'),

                       url(r'^admin/setup/location_2_3_1$', 'location_2_3_1', name='admin_setup_location_2_3_1'),

                       url(r'^admin/setup/location_2_3_2$', 'location_2_3_2', name='admin_setup_location_2_3_2'),

                       url(r'^admin/setup/location_2_3_3$', 'location_2_3_3', name='admin_setup_location_2_3_3'),

                       url(r'^admin/setup/location_2_3_4$', 'location_2_3_4', name='admin_setup_location_2_3_4'),

                       url(r'^admin/setup/location_2_3_4/(?P<location_number>\d+)/$', 'location_2_3_4', name='admin_setup_location_2_3_4_questions'),

                       )
