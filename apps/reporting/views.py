from django.shortcuts import render
from apps.dashboard.models import *
from apps.reporting.models import *
from datetime import datetime
from apps.api.v1.utils.views import *
from itertools import chain
import collections
from django.db.models import Q
from django.utils.datastructures import SortedDict

def index(request):
    
    categories = len(UtilResourceCategories.objects.filter(is_active=True))
    report_categories = UtilReportCategories.objects.filter(is_active=True).order_by("display_priority")
    return render(request,
                  'reporting/index.html',
                  {'request': request,
                   'categories': categories,
                   'report_categories': report_categories,
                   })

#academic views
def academic(request):
    reports = UtilReportCategories.objects.get(is_active=True, report_category='Academic').reports.filter(is_active=True).order_by('display_order')
    return render(request,
                  'reporting/academic/index.html',
                  {'request': request,
                   'reports': reports,
                   })

def academic_org_compliance_summary(request):
    cur_date = datetime.now()
    return render(request, 'reporting/academic/orgcompliance.html', {'request': request, 'currentDate': cur_date})

def academic_org_compliance_detail(request):    
    return render(request, 'reporting/academic/orgcompliance.html', {'request': request})

def academic_loc_compliance_summary(request):
    cur_date = datetime.now()
    return render(request, 'reporting/academic/loccompliance.html', {'request': request, 'currentDate': cur_date})

def academic_loc_compliance_detail(request):
    return render(request, 'reporting/academic/loccompliance.html', {'request': request})

#verified messaging views
def verified_messaging(request):
    reports = UtilReportCategories.objects.get(is_active=True, report_category='Verified Messaging').reports.filter(is_active=True).order_by('display_order')
    return render(request,
                  'reporting/academic/index.html',
                  {'request': request,
                   'reports': reports,
                   })
    #return render(request, 'reporting/verifiedmessaging/index.html', {'request': request})

def message_history_detailed(request):    
    return render(request, 'reporting/verifiedmessaging/messagehistory/detailed.html', {'request': request})

def message_history_detailed_report(request):
    return render(request, 'reporting/verifiedmessaging/messagehistory/report.html', {'request': request})

def message_history_summary(request):
    cur_date = datetime.now()
    return render(request, 'reporting/verifiedmessaging/messagehistory/summary.html', {'request': request, 'currentDate': cur_date})

# Human Resources
def human_resources(request):
    reports = UtilReportCategories.objects.get(is_active=True, report_category='Human Resources').reports.filter(is_active=True).order_by('display_order')
    return render(request,
                  'reporting/human_resources/index.html',
                  {'request': request,
                   'reports': reports,
                   })

# Benchmarking
def benchmarking(request):
    reports = UtilReportCategories.objects.get(is_active=True, report_category='Benchmarking').reports.filter(is_active=True).order_by('display_order')
    return render(request,
                  'reporting/benchmarking/index.html',
                  {'request': request,
                   'reports': reports,
                   })
# Milestones
def milestones(request):
    reports = UtilReportCategories.objects.get(is_active=True, report_category='Milestones').reports.filter(is_active=True).order_by('display_order')
    return render(request,
                  'reporting/milestones/index.html',
                  {'request': request,
                   'reports': reports,
                   })

# CE Licensing
def ce_licensing(request):
    reports = UtilReportCategories.objects.get(is_active=True, report_category='CE/Licensing').reports.filter(is_active=True).order_by('display_order')
    return render(request,
                  'reporting/ce_licensing/index.html',
                  {'request': request,
                   'reports': reports,
                   })

# Resources
def resources(request):
    reports = UtilReportCategories.objects.get(is_active=True, report_category='Resources').reports.filter(is_active=True).order_by('display_order')
    return render(request,
                  'reporting/resources/index.html',
                  {'request': request,
                   'reports': reports,
                   })

# Regulations and Laws
def regs_and_laws(request):
    reports = UtilReportCategories.objects.get(is_active=True, report_category='Regulations/Laws').reports.filter(is_active=True).order_by('display_order')
    return render(request,
                  'reporting/regs_and_laws/index.html',
                  {'request': request,
                   'reports': reports,
                   })

def regs_and_laws_summary(request):
    report = CoreReports.objects.get(report_title='Regulations/Laws Summary')
    cur_date = convert_timezone(datetime.now(), request.user)
    agencies_list = UtilRegAgenciesRegulations.objects.all().values_list('utilregagencies', flat=True).distinct()
    regs_laws_count = UtilRegAgenciesRegulations.objects.count()
    state_count = UtilRegAgencyRegulationsByState.objects.count()
    county_count = UtilRegAgencyRegulationsByCounty.objects.count()
    city_count = UtilRegAgencyRegulationsByCity.objects.count()
    agencies = UtilRegAgencies.objects.filter(id__in=agencies_list).order_by('name')
    copyright_code = replace_tags(request, report.reports_copyright_statements.copyright_statement)

    return render(request,
                  'reporting/regs_and_laws/summary.html',
                  { 'request': request,
                    'cur_date': cur_date,
                    'agencies_count': len(agencies_list),
                    'regs_laws_count': regs_laws_count,
                    'state_count': state_count,
                    'county_count': county_count,
                    'city_count': city_count,
                    'agencies': agencies,
                    'copyright_code': copyright_code,
                   })

def regs_and_laws_resource(request):
    reg_code = request.POST.get("reg", None)
    cur_date = convert_timezone(datetime.now(), request.user)
    report = CoreReports.objects.get(report_title='Regulation/Law By Resource')
    copyright_code = replace_tags(request, report.reports_copyright_statements.copyright_statement)
    if reg_code:
        regulation = UtilRegAgencyRegulations.objects.get(reg_code=reg_code)
        # get courses
        courses = []
        course_ids = CoreCoursesRegulations.objects.filter(utilregagencyregulations=regulation).values_list('corecourses_id', flat=True)
        if len(course_ids) > 0:
            courses = CoreCourses.objects.filter(id__in=course_ids).order_by('number')
        # get forms, publications, videos
        forms = []
        videos = []
        publications = []
        form_ids = []
        video_ids = []
        publication_ids = []

        for course in courses:
            if len(form_ids) == 0:
                form_ids = course.resources.filter(is_form=True, is_active=True).order_by('resource_name').values_list('id', flat=True)
            else:
                ids = course.resources.filter(is_form=True, is_active=True).order_by('resource_name').values_list('id', flat=True)
                form_ids = set(form_ids) - set(ids)
                form_ids = list(chain(form_ids, course.resources.filter(is_form=True, is_active=True).order_by('resource_name').values_list('id', flat=True)))
            if len(video_ids) == 0:
                video_ids = course.resources.filter(is_video=True, is_active=True).order_by('resource_name').values_list('id', flat=True)
            else:
                ids = course.resources.filter(is_video=True, is_active=True).order_by('resource_name').values_list('id', flat=True)
                video_ids = set(video_ids) - set(ids)
                video_ids = list(chain(video_ids, course.resources.filter(is_video=True, is_active=True).order_by('resource_name').values_list('id', flat=True)))
            if len(publication_ids) == 0:
                publication_ids = course.resources.filter(is_publication=True, is_active=True).order_by('resource_name').values_list('id', flat=True)
            else:
                ids = course.resources.filter(is_publication=True, is_active=True).order_by('resource_name').values_list('id', flat=True)
                publication_ids = set(publication_ids) - set(ids)
                publication_ids = list(chain(publication_ids, course.resources.filter(is_publication=True, is_active=True).order_by('resource_name').values_list('id', flat=True)))

        forms = CoreResources.objects.filter(id__in=form_ids).order_by('resource_name')
        videos = CoreResources.objects.filter(id__in=video_ids).order_by('resource_name')
        publications = CoreResources.objects.filter(id__in=publication_ids).order_by('resource_name')

        return render(request,
                  'reporting/regs_and_laws/resource.html',
                  { 'request': request,
                    'cur_date': cur_date,
                    'regulation': regulation,
                    'courses': courses,
                    'forms': forms,
                    'publications': publications,
                    'videos': videos,
                    'copyright_code': copyright_code,
                   })

    agencies_list = UtilRegAgenciesRegulations.objects.all().values_list('utilregagencies', flat=True).distinct()
    agencies = UtilRegAgencies.objects.filter(id__in=agencies_list).order_by('name')

    return render(request,
                  'reporting/regs_and_laws/resource.html',
                  {'request': request,
                   'agencies': agencies,
                   'copyright_code': copyright_code,
                   })

# Accreditation
def accreditation(request):
    reports = UtilReportCategories.objects.get(is_active=True, report_category='Accreditation').reports.filter(is_active=True).order_by('display_order')

    return render(request,
                  'reporting/accreditation/index.html',
                  {'request': request,
                   'reports': reports,
                   })

def accreditation_standard_summary(request):
    agency_id = request.POST.get("org", None)
    date = request.POST.get("date", None)
    report = CoreReports.objects.get(report_title='Accreditation Standards Summary')
    copyright_code = replace_tags(request, report.reports_copyright_statements.copyright_statement)
    cur_date = datetime.now()
    st_data = SortedDict()
    #agency_id="586"
    if agency_id is not None and agency_id != "":
        cur_date = datetime.strptime(date, '%d-%B-%Y')
        accreditation_agency = UtilRegAgencies.objects.get(id=agency_id)
        disclaimer = CoreReportsDisclaimerStatements.objects.get(reg_agencies_id=accreditation_agency.id)
        disclaimer_statement = replace_tags(request, disclaimer.disclaimer_statement)

        if accreditation_agency.id == 11:
            categories = AccreditingAgencyAchcCategories.objects.filter(is_active=True).values_list('category_name', flat=True)
            subcategories = AccreditingAgencyAchcSubCategories.objects.filter(is_active=True)
            elements = AccreditingAgencyAchc.objects.filter(Q(effective_date__lte=cur_date) & (Q(deactiviation_date=None) | Q(deactiviation_date__lte=cur_date)))\
                .order_by('achc_categories__id', 'short_code')
            standards_count = elements.count()
            for standard in elements:
                key = standard.achc_categories.category_name + " (" + standard.achc_categories.short_code + ")"
                if key not in st_data:
                    st_data[key] = []
                st_data[key].append({'id': standard.id,
                                    'description': standard.standard_number + ": " + standard.standrard_description,
                                    'effective_date': standard.effective_date})

            return render(request,
                  'reporting/accreditation/standard_summary.html',
                  {'request': request,
                   'accreditation_agency': accreditation_agency,
                   'categories_count': categories.count(),
                   'subcategories_count': subcategories.count(),
                   'copyright_code': copyright_code,
                   'cur_date': cur_date,
                   'standards': st_data,
                   'standards_count': standards_count,
                   'disclaimer': disclaimer_statement
                   })

        elif accreditation_agency.id == 9:
            categories = AccreditingAgencyTjcCategories.objects.filter(is_active=True)
            standards = AccreditingAgencyTjcStandards.objects.filter(is_active=True)
            elements = AccreditingAgencyTjcElements.objects.filter(Q(effective_date__lte=cur_date) & (Q(deactivation_date=None) | Q(deactivation_date__gte=cur_date))).order_by('util_accrediting_agency_tjc_standards__tjc_categories__id','short_code')
            for standard in elements:
                key = standard.util_accrediting_agency_tjc_standards.tjc_categories.category_name + " (" + standard.util_accrediting_agency_tjc_standards.tjc_categories.short_code + ")"
                if key not in st_data:
                    st_data[key] = SortedDict()
                key1 = standard.util_accrediting_agency_tjc_standards.standard_number + ": " + standard.util_accrediting_agency_tjc_standards.standard_description
                if key1 not in st_data[key]:
                    st_data[key][key1] = []
                st_data[key][key1].append({'id': standard.id,
                                    'description': standard.element_of_performance_number + ": " + standard.element_description,
                                    'effective_date': standard.effective_date})

            return render(request,
                  'reporting/accreditation/standard_summary.html',
                  {'request': request,
                   'accreditation_agency': accreditation_agency,
                   'categories_count': categories.count(),
                   'subcategories_count': standards.count(),
                   'copyright_code': copyright_code,
                   'cur_date': cur_date,
                   'standards': st_data,
                   'standards_count': len(elements),
                   'disclaimer': disclaimer_statement
                   })

        elif accreditation_agency.id == 586:
            categories = AccreditingAgencyHqaaCategories.objects.filter(is_active=True)
            subcategories = AccreditingAgencyHqaaSubcategories.objects.filter(is_active=True)
            elements = AccreditingAgencyHqaa.objects.filter(Q(effective_date__lte=cur_date) & (Q(deactivation_date=None) | Q(deactivation_date__gte=cur_date)))\
                .order_by('hqaa_subcategories__id', 'short_code')
            standards_count = len(elements)
            for standard in elements:
                key = standard.hqaa_subcategories.hqaa_categories.category_name
                if key not in st_data:
                    st_data[key] = SortedDict()
                key1 = standard.hqaa_subcategories.subcategory_name# + " (" + standard.hqaa_subcategories.short_code + ")"
                if key1 not in st_data[key]:
                    st_data[key][key1] = []
                st_data[key][key1].append({'id': standard.id,
                                    'description': standard.standard_number + ": " + standard.standard_description,
                                    'effective_date': standard.effective_date})
            return render(request,
                  'reporting/accreditation/standard_summary.html',
                  {'request': request,
                   'accreditation_agency': accreditation_agency,
                   'categories_count': categories.count(),
                   'subcategories_count': subcategories.count(),
                   'copyright_code': copyright_code,
                   'cur_date': cur_date,
                   'standards': st_data,
                   'standards_count': standards_count,
                   'disclaimer': disclaimer_statement
                   })

        elif accreditation_agency.id == 587:
            categories_count = AccreditingAgencyCteamCategories.objects.filter(is_active=True).count()
            subcategories_count = AccreditingAgencyCteamSubcategories.objects.filter(is_active=True).count()
            standards_count = AccreditingAgencyCteamStandards.objects.filter(is_active=True).count()
            elements = AccreditingAgencyCteamEvidenceOfCompliance.objects.filter(Q(effective_date__lte=cur_date) & (Q(deactivation_date=None) | Q(deactivation_date__gte=cur_date)))\
                .order_by('accrediting_agency_cteam_standards__cteam_subcategories__cteam_categories__id', 'accrediting_agency_cteam_standards__cteam_subcategories__id', 'short_code')
            for standard in elements:
                st = standard.accrediting_agency_cteam_standards
                subcategory = st.cteam_subcategories
                category = subcategory.cteam_categories
                key = category.category_name
                if key not in st_data:
                    st_data[key] = SortedDict()
                key1 = subcategory.subcategory_name + " (" + subcategory.short_code + ")"
                if key1 not in st_data[key]:
                    st_data[key][key1] = SortedDict()
                key2 = st.standard_number + ": " + st.standard_description
                if key2 not in st_data[key][key1]:
                    st_data[key][key1][key2] = []
                st_data[key][key1][key2].append({'id': standard.id,
                                    'description': standard.evidence_of_compliance_number + ": " + standard.evidence_of_compliane_description,
                                    'effective_date': standard.effective_date})

            return render(request,
              'reporting/accreditation/standard_summary.html',
              {'request': request,
               'accreditation_agency': accreditation_agency,
               'categories_count': categories_count,
               'subcategories_count': subcategories_count,
               'standards_count': standards_count,
               'sub_standards_count': elements.count(),
               'copyright_code': copyright_code,
               'cur_date': cur_date,
               'standards': st_data,
               'disclaimer': disclaimer_statement
               })

        elif accreditation_agency.id == 588:
            categories_count = AccreditingAgencyBocCategories.objects.filter(is_active=True).count()
            subcategories_count = AccreditingAgencyBocSubcategories.objects.filter(is_active=True).count()
            standards_count = AccreditingAgencyBoc.objects.filter(is_active=True).count()
            elements = AccreditingAgencyBocStandards.objects.filter(Q(effective_date__lte=cur_date) & (Q(deactivation_date=None) | Q(deactivation_date__gte=cur_date))).order_by('short_code')
            for standard in elements:
                boc = standard.accrediting_agency_boc
                subcategory = boc.accrediting_agency_boc_subcategories
                category = subcategory.boc_categories
                key = category.category_name
                if key not in st_data:
                    st_data[key] = dict()
                key1 = subcategory.subcategory_name + " (" + subcategory.short_code + ")"
                if key1 not in st_data[key]:
                    st_data[key][key1] = dict()
                key2 = boc.standard_description + " (" + boc.standard_number + ")"
                if key2 not in st_data[key][key1]:
                    st_data[key][key1][key2] = []
                st_data[key][key1][key2].append({'id': standard.id,
                                    'description': standard.sub_standard_number + ": " + standard.standard_description,
                                    'effective_date': standard.effective_date})

            return render(request,
                  'reporting/accreditation/standard_summary.html',
                  {'request': request,
                   'accreditation_agency': accreditation_agency,
                   'categories_count': categories_count,
                   'subcategories_count': subcategories_count,
                   'standards_count': standards_count,
                   'sub_standards_count': elements.count(),
                   'copyright_code': copyright_code,
                   'cur_date': cur_date,
                   'standards': st_data,
                   'disclaimer': disclaimer_statement
                   })



    locations = CoreLocations.objects.all().exclude(accreditation_agency_id=None).values_list('accreditation_agency_id', flat=True).distinct()
    departments = CoreDepartments.objects.all().exclude(accreditation_agency_id=None).values_list('accreditation_agency_id', flat=True).distinct()

    # get accreditation agency ids which has location or departments
    accreditation_ids = set(locations) - set(departments)
    accreditation_ids = list(chain(accreditation_ids, departments))

    # get accreditation agencies
    accreditations = UtilRegAgencies.objects.filter(id__in=accreditation_ids).order_by('name')


    return render(request,
                  'reporting/accreditation/standard_summary.html',
                  {'request': request,
                   'accreditations': accreditations,
                   })

def accreditation_standard_resource(request):
    agency_id = request.POST.get("org", None)
    standard_id = request.POST.get("standard", None)

    cur_date = convert_timezone(datetime.now(), request.user)
    report = CoreReports.objects.get(report_title='Accreditation Standard By Resource')
    copyright_code = replace_tags(request, report.reports_copyright_statements.copyright_statement)

    if agency_id is not None:
        accreditation_agency = UtilRegAgencies.objects.get(id=agency_id)
        element_ids = []
        if accreditation_agency.id == 11:
            element_ids = CoreCoursesAccreditationStandardsAchc11.objects.filter(achc_id=standard_id).values_list('courses_id', flat=True)
            standard = AccreditingAgencyAchc.objects.get(id=standard_id)
        elif accreditation_agency.id == 9:
            element_ids = CoreCoursesAccreditationStandardsTjc9.objects.filter(tjc_elements_id=standard_id).values_list('courses_id', flat=True)
            standard = AccreditingAgencyTjcElements.objects.get(id=standard_id)
        elif accreditation_agency.id == 586:
            element_ids = CoreCoursesAccreditationStandardsHqaa586.objects.filter(hqaa_id=standard_id).values_list('courses_id', flat=True)
            standard = AccreditingAgencyHqaa.objects.get(id=standard_id)
        elif accreditation_agency.id == 587:
            element_ids = CoreCoursesAccreditationStandardsCteam587.objects.filter(cteam_evidence_of_compliance_id=standard_id).values_list('courses_id', flat=True)
            standard = AccreditingAgencyCteamEvidenceOfCompliance.objects.get(id=standard_id)
        elif accreditation_agency.id == 588:
            element_ids = CoreCoursesAccreditationStandardsBoc588.objects.filter(boc_standards_id=standard_id).values_list('courses_id', flat=True)
            standard = AccreditingAgencyBocStandards.objects.get(id=standard_id)

        # get courses
        courses = []
        if len(element_ids) > 0:
            courses = CoreCourses.objects.filter(id__in=element_ids).order_by('number')
        # get forms, publications, videos
        forms = []
        videos = []
        publications = []
        form_ids = []
        video_ids = []
        publication_ids = []

        for course in courses:
            if len(form_ids) == 0:
                form_ids = course.resources.filter(is_form=True, is_active=True).order_by('resource_name').values_list('id', flat=True)
            else:
                ids = course.resources.filter(is_form=True, is_active=True).order_by('resource_name').values_list('id', flat=True)
                form_ids = set(form_ids) - set(ids)
                form_ids = list(chain(form_ids, course.resources.filter(is_form=True, is_active=True).order_by('resource_name').values_list('id', flat=True)))
            if len(video_ids) == 0:
                video_ids = course.resources.filter(is_video=True, is_active=True).order_by('resource_name').values_list('id', flat=True)
            else:
                ids = course.resources.filter(is_video=True, is_active=True).order_by('resource_name').values_list('id', flat=True)
                video_ids = set(video_ids) - set(ids)
                video_ids = list(chain(video_ids, course.resources.filter(is_video=True, is_active=True).order_by('resource_name').values_list('id', flat=True)))
            if len(publication_ids) == 0:
                publication_ids = course.resources.filter(is_publication=True, is_active=True).order_by('resource_name').values_list('id', flat=True)
            else:
                ids = course.resources.filter(is_publication=True, is_active=True).order_by('resource_name').values_list('id', flat=True)
                publication_ids = set(publication_ids) - set(ids)
                publication_ids = list(chain(publication_ids, course.resources.filter(is_publication=True, is_active=True).order_by('resource_name').values_list('id', flat=True)))

        forms = CoreResources.objects.filter(id__in=form_ids).order_by('resource_name')
        videos = CoreResources.objects.filter(id__in=video_ids).order_by('resource_name')
        publications = CoreResources.objects.filter(id__in=publication_ids).order_by('resource_name')

        return render(request,
                  'reporting/accreditation/standard_resource.html',
                  { 'request': request,
                    'cur_date': cur_date,
                    'accreditation_agency': accreditation_agency,
                    'courses': courses,
                    'standard': standard,
                    'forms': forms,
                    'publications': publications,
                    'videos': videos,
                    'copyright_code': copyright_code,
                   })

    locations = CoreLocations.objects.all().exclude(accreditation_agency_id=None).values_list('accreditation_agency_id', flat=True).distinct()
    departments = CoreDepartments.objects.all().exclude(accreditation_agency_id=None).values_list('accreditation_agency_id', flat=True).distinct()

    # get accreditation agency ids which has location or departments
    accreditation_ids = set(locations) - set(departments)
    accreditation_ids = list(chain(accreditation_ids, departments))

    # get accreditation agencies
    accreditations = UtilRegAgencies.objects.filter(id__in=accreditation_ids).order_by('name')

    data = dict()
    #get accreditation standards
    for accreditation_agency in accreditations:
        st_data = dict()
        #case agency id is 11
        if accreditation_agency.id == 11:
            element_ids = CoreCoursesAccreditationStandardsAchc11.objects.filter(is_active=1).values_list('achc_id', flat=True)
            elements = AccreditingAgencyAchc.objects.filter(id__in=element_ids).order_by('standard_number')
            for standard in elements:
                if standard.achc_categories.category_name not in st_data:
                    st_data[standard.achc_categories.category_name] = []
                st_data[standard.achc_categories.category_name].append({'id': standard.id, 'value':standard.standard_number})

        elif accreditation_agency.id == 9:
            element_ids = CoreCoursesAccreditationStandardsTjc9.objects.filter(is_active=1).values_list('tjc_elements_id', flat=True)
            elements = AccreditingAgencyTjcElements.objects.filter(id__in=element_ids).order_by('element_of_performance_number')
            for standard in elements:
                if standard.util_accrediting_agency_tjc_standards.tjc_categories.category_name not in st_data:
                    st_data[standard.util_accrediting_agency_tjc_standards.tjc_categories.category_name] = dict()
                if standard.util_accrediting_agency_tjc_standards.standard_number not in st_data[standard.util_accrediting_agency_tjc_standards.tjc_categories.category_name]:
                    st_data[standard.util_accrediting_agency_tjc_standards.tjc_categories.category_name][standard.util_accrediting_agency_tjc_standards.standard_number] = []
                st_data[standard.util_accrediting_agency_tjc_standards.tjc_categories.category_name][standard.util_accrediting_agency_tjc_standards.standard_number].append({'id': standard.id, 'value':standard.element_of_performance_number})

        elif accreditation_agency.id == 586:
            element_ids = CoreCoursesAccreditationStandardsHqaa586.objects.filter(is_active=1).values_list('hqaa_id', flat=True)
            elements = AccreditingAgencyHqaa.objects.filter(id__in=element_ids).order_by('standard_number')
            for standard in elements:
                if standard.hqaa_subcategories.subcategory_name not in st_data:
                    st_data[standard.hqaa_subcategories.subcategory_name] = []
                st_data[standard.hqaa_subcategories.subcategory_name].append({'id': standard.id, 'value':standard.standard_number})

        elif accreditation_agency.id == 587:
            element_ids = CoreCoursesAccreditationStandardsCteam587.objects.filter(is_active=1).values_list('cteam_evidence_of_compliance_id', flat=True)
            elements = AccreditingAgencyCteamEvidenceOfCompliance.objects.filter(id__in=element_ids).order_by('evidence_of_compliance_number')
            for standard in elements:
                key = standard.accrediting_agency_cteam_standards.cteam_subcategories.subcategory_name
                if  key not in st_data:
                    st_data[key] = dict()
                key1 = standard.accrediting_agency_cteam_standards.standard_number
                if  key1 not in st_data[key]:
                    st_data[key][key1] = []
                st_data[key][key1].append({'id': standard.id, 'value':standard.evidence_of_compliance_number})

        elif accreditation_agency.id == 588:
            element_ids = CoreCoursesAccreditationStandardsBoc588.objects.filter(is_active=1).values_list('boc_standards_id', flat=True)
            elements = AccreditingAgencyBocStandards.objects.filter(id__in=element_ids).order_by('sub_standard_number')
            for standard in elements:
                if standard.accrediting_agency_boc.standard_description not in st_data:
                    st_data[standard.accrediting_agency_boc.standard_description] = []
                st_data[standard.accrediting_agency_boc.standard_description].append({'id': standard.id, 'value':standard.sub_standard_number})

        data[accreditation_agency.id] = collections.OrderedDict(sorted(st_data.items()))

    return render(request,
              'reporting/accreditation/standard_resource.html',
              {'request': request,
               'accreditations': accreditations,
                'standards': data,
               })

# Inservices
def inservices(request):
    reports = UtilReportCategories.objects.get(is_active=True, report_category='Inservices').reports.filter(is_active=True).order_by('display_order')
    return render(request,
                  'reporting/inservices/index.html',
                  {'request': request,
                   'reports': reports,
                   })

# LMS Crosswalks
def lms_crosswalks(request):
    reports = UtilReportCategories.objects.get(is_active=True, report_category='LMS Crosswalks').reports.filter(is_active=True).order_by('display_order')
    return render(request,
                  'reporting/lms_crosswalks/index.html',
                  {'request': request,
                   'reports': reports,
                   })

# Administration
def administration(request):
    reports = UtilReportCategories.objects.get(is_active=True, report_category='Administration').reports.filter(is_active=True).order_by('display_order')
    return render(request,
                  'reporting/administration/index.html',
                  {'request': request,
                   'reports': reports,
                   })
