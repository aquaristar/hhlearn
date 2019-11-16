from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.admin.tests.views',
                       
                       url(r'^admin/tests/$', 'home', name='admin_tests_home'),
                       url(r'^admin/tests/add/$', 'add', name='admin_tests_add'), 
                       url(r'^admin/tests/edit/(?P<test_id>.+)?$', 'edit', name='admin_tests_edit'),                                                                    
                       )
