from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.admin.setup.organization.views',

                       url(r'^admin/setup/organization_1_1$', 'organization_1_1', name='admin_setup_organization_1_1'),

                       url(r'^admin/setup/organization_1_2$', 'organization_1_2', name='admin_setup_organization_1_2'),

                       url(r'^admin/setup/organization_1_3$', 'organization_1_3', name='admin_setup_organization_1_3'),

                       url(r'^admin/setup/organization_1_4$', 'organization_1_4', name='admin_setup_organization_1_4'),

                       url(r'^admin/setup/organization_1_5$', 'organization_1_5', name='admin_setup_organization_1_5'),
                       
                       url(r'^admin/setup/organization_1_6$', 'organization_1_6', name='admin_setup_organization_1_6'),

                       url(r'^admin/setup/organization_1_7/$', 'organization_1_7', name='admin_setup_organization_1_7'),

                       url(r'^admin/setup/organization_1_7/(?P<question_start>\d+)/(?P<question_end>\d+)/$', 'organization_1_7', name='admin_setup_organization_1_7_questions'),


                       )
