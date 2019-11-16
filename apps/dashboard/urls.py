from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('apps.dashboard.views',

                       #url(r'^contactus/$', 'contactus', name='contactus'),
                       url(r'^dashboard/milestones/$', 'milestones', name='milestones'),
                       
)
urlpatterns += patterns('apps.dashboard.core.views',

                       #url(r'^dashboard/$', 'home', name='home'),
                       (r'', include('apps.dashboard.home.urls')),
                       (r'', include('apps.dashboard.profile.urls')),
                       (r'', include('apps.dashboard.accreditation.urls')),
                       (r'', include('apps.dashboard.assignments.urls')),
                       (r'', include('apps.dashboard.documents.urls')),
                       (r'', include('apps.dashboard.history.urls')),
                       (r'', include('apps.dashboard.messages.urls')),
                       (r'', include('apps.dashboard.metrics.urls')),
                       (r'', include('apps.dashboard.auth.urls')),                       
                       (r'', include('apps.dashboard.courses.urls')),
                       (r'', include('apps.dashboard.sandbox.urls')),
                       (r'', include('apps.dashboard.tests.urls')),
                       (r'', include('apps.dashboard.certificate.urls')),
                       (r'', include('apps.dashboard.tasks.urls')),
                       (r'', include('apps.dashboard.alerts.urls')),

                       #url(r'^dashboard/$', RedirectView.as_view(url='/dashboard/assignments'), name='dashboard'),

                       )
