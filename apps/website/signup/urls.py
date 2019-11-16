from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.signup.views',

                       url(r'^signup/$', 'signup', name='signup'),

                       url(r'^signup/terms/$', 'signup_terms', name='signup_terms'),

                       url(r'^signup/payment/$', 'signup_payment', name='signup_payment'),

                       url(r'^signup/thank_you/$', 'signup_thank_you', name='signup_thank_you'),

                        # this URL will only support alphanumeric 10 characters long string only.
                       url(r'^signup/confirm_email/(\w{10})/$', 'signup_confirm_email', name='confirm_email'),

                       )