from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

                       (r'', include('apps.api.v1.auth.urls')),
                       (r'', include('apps.api.v1.documents.urls')),
                       (r'', include('apps.api.v1.courses.urls')),
                       (r'', include('apps.api.v1.profile.urls')),
                       (r'', include('apps.api.v1.assignments.urls')),
                       (r'', include('apps.api.v1.tests.urls')),
                       (r'', include('apps.api.v1.history.urls')),
                       (r'', include('apps.api.v1.metrics.urls')),                       
                       (r'', include('apps.api.v1.alerts.urls')),
                       (r'', include('apps.api.v1.messages.urls')),
                       (r'', include('apps.api.v1.tasks.urls')),
                       (r'', include('apps.api.v1.users.urls')),

)