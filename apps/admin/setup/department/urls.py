from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.admin.setup.department.views',

                       url(r'^admin/setup/department_3$', 'department_3', name='admin_setup_department_3'),

                       url(r'^admin/setup/department_3_1$', 'department_3_1', name='admin_setup_department_3_1'),

                       url(r'^admin/setup/department_3_1_1$', 'department_3_1_1', name='admin_setup_department_3_1_1'),

                       url(r'^admin/setup/department_3_1_1/(?P<location_number>\d+)/$', 'department_3_1_1', name='admin_setup_department_3_1_1_questions'),

                       url(r'^admin/setup/department_3_1_2$', 'department_3_1_2', name='admin_setup_department_3_1_2'),

                       url(r'^admin/setup/department_3_1_2/(?P<location_number>\d+)/$', 'department_3_1_2', name='admin_setup_department_3_1_2_questions'),

                       url(r'^admin/setup/department_3_1_3$', 'department_3_1_3', name='admin_setup_department_3_1_3'),

                       url(r'^admin/setup/department_3_1_3/(?P<location_number>\d+)/$', 'department_3_1_3', name='admin_setup_department_3_1_3_questions'),

                       url(r'^admin/setup/department_3_1_4$', 'department_3_1_4', name='admin_setup_department_3_1_4'),

                       url(r'^admin/setup/department_3_1_4/(?P<location_number>\d+)/$', 'department_3_1_4', name='admin_setup_department_3_1_4_questions'),

                       url(r'^admin/setup/department_3_1_5$', 'department_3_1_5', name='admin_setup_department_3_1_5'),

                       url(r'^admin/setup/department_3_1_5/(?P<location_number>\d+)/(?P<department_number>\d+)/$', 'department_3_1_5', name='admin_setup_department_3_1_5_questions'),

                       )
