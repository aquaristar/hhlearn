from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('',

                       url(r'^$', 'apps.website.home.views.home', name='landing_page')
)

urlpatterns += patterns('apps.website.views',

                        #include all URLs for website

                        (r'', include('apps.website.benefits.urls')),
                        (r'', include('apps.website.choose_edition.urls')),
                        (r'', include('apps.website.code_of_conduct.urls')),
                        (r'', include('apps.website.compliance.urls')),
                        (r'', include('apps.website.contact.urls')),
                        (r'', include('apps.website.courses.urls')),
                        (r'', include('apps.website.demos.urls')),
                        (r'', include('apps.website.faq.urls')),
                        (r'', include('apps.website.features.urls')),
                        (r'', include('apps.website.home.urls')),
                        (r'', include('apps.website.login.urls')),
                        (r'', include('apps.website.news.urls')),
                        (r'', include('apps.website.newsletter.urls')),
                        (r'', include('apps.website.our_modules.urls')),
                        (r'', include('apps.website.our_testing.urls')),
                        (r'', include('apps.website.plan_details.urls')),
                        (r'', include('apps.website.plans.urls')),
                        (r'', include('apps.website.pricing.urls')),
                        (r'', include('apps.website.privacy.urls')),
                        (r'', include('apps.website.register.urls')),
                        #(r'', include('apps.website.reporting.urls')),
                        (r'', include('apps.website.sample.urls')),
                        (r'', include('apps.website.signup.urls')),
                        (r'', include('apps.website.terms.urls')),
                        (r'', include('apps.website.testimonials.urls')),
                        (r'', include('apps.website.thank_you.urls')),
                        (r'', include('apps.website.sandbox.urls')),

)
