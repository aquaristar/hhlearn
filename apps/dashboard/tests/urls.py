from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.tests.views',

                       # URL must have the encypted course code.
                       url(r'^dashboard/test/(?P<test_code_encrypted>.+)?$', 'test', name='dashboard_tests'),
                       
                       # URL must have the encypted course code.
                       url(r'^dashboard/testresult/(?P<test_attempt_code_encrypted>.+)?$', 'test_result', name='dashboard_test_result'),                       

                       )
