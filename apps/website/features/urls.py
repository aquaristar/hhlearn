from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.features.views',

                       url(r'^features/benefits', 'features_benefits', name='features_benefits'),
                       url(r'^features/courses$', 'features_courses', name='features_courses'),
                       url(r'^features/responsive$', 'features_responsive', name='features_responsive'),
                       url(r'^features/terms$', 'features_terms', name='features_terms'),

                       )