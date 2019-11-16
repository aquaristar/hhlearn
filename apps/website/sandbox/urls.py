from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.sandbox.views',                       
                       url(r'^sandbox/countdown$', 'countdown', name='countdown'),
                       url(r'^sandbox/loginhome$', 'loginhome', name='loginhome'),
                       url(r'^sandbox/signup/step1$', 'signup_step1', name='signup_step1'),
                       url(r'^sandbox/signup/step2$', 'signup_step2', name='signup_step2'),
                       url(r'^sandbox/signup/step3$', 'signup_step3', name='signup_step3'),
                       url(r'^sandbox/signup/step4$', 'signup_step4', name='signup_step4'),
                       url(r'^sandbox/features$', 'features', name='features'),
                       url(r'^sandbox/features_page2$', 'features_page2', name='features_page2'),
                       url(r'^sandbox/features_page3$', 'features_page3', name='features_page3'),
                       url(r'^sandbox/features_page4$', 'features_page4', name='features_page4'),                       
                       url(r'^sandbox/features_page5$', 'features_page5', name='features_page5'),                       
                       url(r'^sandbox/faqs$', 'faqs', name='faqs'),
                       url(r'^sandbox/other_book$', 'other_book', name='other_book'),
                       url(r'^sandbox/terms$', 'terms', name='terms'),
                       url(r'^sandbox/page811$', 'page811', name='page811'),
                       )
