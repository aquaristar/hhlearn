from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView


urlpatterns = patterns('apps.reporting.views',
                        url(r'^reporting/$', 'index', name='reporting_home'),
                        # Academic
                        url(r'^reporting/academic/$', 'academic', name='reporting_academic'),
                        url(r'^reporting/academic/orgcompliancesummary$', 'academic_org_compliance_summary', name='reporting_academic_org_compliance_summary'),
                        url(r'^reporting/academic/loccompliancesummary$', 'academic_loc_compliance_summary', name='reporting_academic_loc_compliance_summary'),
                        # Verified message
                        url(r'^reporting/verifiedmessaging/$', 'verified_messaging', name='reporting_verified_messaging'),
                        url(r'^reporting/verifiedmessaging/messagehistory/detailed/$', 'message_history_detailed', name='message_history_detailed'),
                        url(r'^reporting/verifiedmessaging/messagehistory/detailed/report$', 'message_history_detailed_report', name='message_history_detailed_report'),
                        url(r'^reporting/verifiedmessaging/messagehistory/summary$', 'message_history_summary', name='message_history_summary'),
                        # Human resources
                        url(r'^reporting/hr/$', 'human_resources', name='reporting_human_resources'),
                        # Benchmarking
                        url(r'^reporting/benchmarking/$', 'benchmarking', name='reporting_benchmarking'),
                        # Milestones
                        url(r'^reporting/milestones/$', 'milestones', name='reporting_milestones'),
                        # CE Licensing
                        url(r'^reporting/ce_licensing/$', 'ce_licensing', name='reporting_ce_licensing'),
                        # Resources
                        url(r'^reporting/resources/$', 'resources', name='reporting_resources'),
                        # Regulations and Laws
                        url(r'^reporting/regs_and_laws/$', 'regs_and_laws', name='reporting_regs_and_laws'),
                        url(r'^reporting/regs_and_laws/regs_and_laws_summary/$', 'regs_and_laws_summary', name='reporting_regs_and_laws_summary'),
                        url(r'^reporting/regs_and_laws/regs_and_laws_resource/$', 'regs_and_laws_resource', name='reporting_regs_and_laws_resource'),
                        # Accreditation
                        url(r'^reporting/accreditation/$', 'accreditation', name='reporting_accreditation'),
                        url(r'^reporting/accreditation/standard_summary/$', 'accreditation_standard_summary', name='reporting_accreditation_standard_summary'),
                        url(r'^reporting/accreditation/standard_resource/$', 'accreditation_standard_resource', name='reporting_accreditation_standard_resource'),

                        # Inservices
                        url(r'^reporting/inservices/$', 'inservices', name='reporting_inservices'),
                        # LMS Crosswalks
                        url(r'^reporting/lms_crosswalks/$', 'lms_crosswalks', name='reporting_lms_crosswalks'),
                        # Administration
                        url(r'^reporting/administration/$', 'administration', name='reporting_administration'),

                       )
