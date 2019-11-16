from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.sandbox.views',

                       url(r'^dashboard/sandbox/test_page$', 'test_page', name='test_page'),
                       url(r'^dashboard/sandbox/sample1$', 'sample1', name='sample1'),
                       url(r'^dashboard/sandbox/countdown$', 'countdown', name='countdown'),

                       )
