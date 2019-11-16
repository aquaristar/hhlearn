from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.dashboard.certificate.views',

                       # URL must have the encypted course code.
                       url(r'^certificate/pdf/(?P<cert_code_encrypted>.+)?$', 'certificate', name='dashboard_certificate_pdf'),
                       url(r'^certificate/pdf_report/(?P<cert_code_encrypted>.+)?$', 'certificate_report', name='dashboard_certificate_pdf_report'),
                       url(r'^certificate/result', 'result', name='dashboard_certificate_result'),
                       url(r'^scoc/(?P<cert_code_encrypted>.+)?$', 'verficiation', name='dashboard_certificate_scoc'),
                       url(r'^scocd/(?P<cert_code_encrypted>.+)?$', 'verficiation_additional', name='dashboard_certificate_scocd'),
                                              
                       )
