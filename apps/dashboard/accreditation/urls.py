from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.accreditation.views',

                       url(r'^dashboard/accreditation/$', 'accreditation', name='accreditation'),

                       )
