# Importing render module from django
from django.shortcuts import render

from django.core.urlresolvers import reverse


# Importing redirect module from django.
from django.http import HttpResponseRedirect

from apps.utility.models import *

from apps.dashboard.models import *

from django.forms.formsets import formset_factory

from django.utils.functional import curry

from forms import *


def location_2_1(request):

    global back_button_url

    organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

    total_active_locations_to_ask = organization.total_number_of_locations

    Location_2_1_Formset = formset_factory(Location_2_1, can_delete=False, can_order=False, max_num=total_active_locations_to_ask,  extra=total_active_locations_to_ask)

    list_of_locations = organization.locations.filter(core_organization__id=organization.id).order_by('id').values('id', 'short_name', 'street_address_1',  'street_address_2', 'city', 'state', 'zip_code', 'phone', 'fax', 'is_primary', 'is_command_location')

    # if request if POST then we need to process the form.
    if request.method == 'POST':

        formset = Location_2_1_Formset(request.POST)

        if formset.is_valid():

            for form in formset:

                print 'validation passed'

                location_already_in_db = organization.locations.filter(core_organization__id=organization.id, id=form.cleaned_data['id']).exists()

                if location_already_in_db is False:

                    location = CoreLocations()

                    location.short_name = form.cleaned_data['short_name']

                    location.street_address_1 = form.cleaned_data['street_address_1']

                    location.street_address_2 = form.cleaned_data['street_address_2']

                    location.city = form.cleaned_data['city']

                    location.state = form.cleaned_data['state'].name

                    location.zip_code = form.cleaned_data['zip_code']

                    location.phone = form.cleaned_data['phone']

                    location.fax = form.cleaned_data['fax']

                    location.is_primary = form.cleaned_data['is_primary']

                    location.is_command_location = form.cleaned_data['is_command_location']

                    location.is_active = 1

                    location.save()

                    organization.locations.add(location)

                elif location_already_in_db is True:

                    location = organization.locations.get(core_organization__id=organization.id, id=form.cleaned_data['id'])

                    location.short_name = form.cleaned_data['short_name']

                    location.street_address_1 = form.cleaned_data['street_address_1']

                    location.street_address_2 = form.cleaned_data['street_address_2']

                    location.city = form.cleaned_data['city']

                    location.state = form.cleaned_data['state'].name

                    location.zip_code = form.cleaned_data['zip_code']

                    location.phone = form.cleaned_data['phone']

                    location.fax = form.cleaned_data['fax']

                    location.is_primary = form.cleaned_data['is_primary']

                    location.is_command_location = form.cleaned_data['is_command_location']

                    location.is_active = 1

                    location.save()

            return HttpResponseRedirect(reverse('admin_setup_location_2_2'))

        else:

            """
            START :: Back URL Part
            """

            total_active_officials_to_ask = UtilOfficialTypes.objects.filter(is_active=1).count()

            DEFAULT_officials_per_page = CoreSettings.objects.get(short_code__exact='DEFAULT_questions_per_page').value

            back_question_start = int(total_active_officials_to_ask+1) - int(DEFAULT_officials_per_page)

            back_question_end = int(total_active_officials_to_ask)

            back_button_url = reverse('admin_setup_organization_1_7_questions', args=(back_question_start, back_question_end))

            """
            END :: Back URL Part
            """

            print 'validation failed'

    # if request is NOT post then lets load form simply
    else:

        """
        START :: Back URL Part
        """

        total_active_officials_to_ask = UtilOfficialTypes.objects.filter(is_active=1).count()

        DEFAULT_officials_per_page = CoreSettings.objects.get(short_code__exact='DEFAULT_questions_per_page').value

        back_question_start = int(total_active_officials_to_ask+1) - int(DEFAULT_officials_per_page)

        back_question_end = int(total_active_officials_to_ask)

        back_button_url = reverse('admin_setup_organization_1_7_questions', args=(back_question_start, back_question_end))

        """
        END :: Back URL Part
        """

        formset = Location_2_1_Formset(initial=list_of_locations)

    # At the end we need to render the page and pass our form :)
    return render(request, 'admin/setup/location/location_2_1.html', {
        'formset': formset,
        'request': request,
        'back_button_url': back_button_url,
        'organization': organization
    })


def location_2_2(request):

    organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

    total_active_locations_to_ask = organization.total_number_of_locations

    Location_2_2_Formset = formset_factory(Location_2_2, can_delete=False, can_order=False, max_num=total_active_locations_to_ask,  extra=total_active_locations_to_ask)

    Location_2_2_Formset.form = staticmethod(curry(Location_2_2, organization=organization))

    list_of_locations = organization.locations.filter(core_organization__id=organization.id).order_by('id').values('id', 'short_name', 'hippa_notice_location',  'emergency_location', 'use_electronic_posting', 'is_accredited', 'accreditation_agency')

    # if request if POST then we need to process the form.
    if request.method == 'POST':

        formset = Location_2_2_Formset(request.POST)

        if formset.is_valid():

            for form in formset:

                print 'validation passed'

                location_already_in_db = organization.locations.filter(core_organization__id=organization.id, id=form.cleaned_data['id']).exists()

                if location_already_in_db is False:

                    location = CoreLocations()

                    location.hippa_notice_location = form.cleaned_data['hippa_notice_location']

                    location.emergency_location = form.cleaned_data['emergency_location']

                    if organization.is_electronic_postings_enabled.value == 1 and organization.is_electronic_postings_consistent.value == 0:

                        location.use_electronic_posting = form.cleaned_data['use_electronic_posting']

                    else:

                        location.use_electronic_posting = organization.is_electronic_postings_enabled

                    if organization.is_organization_accredited.value == 1 and organization.is_accredited_by_same_agency.value == 0:

                        location.is_accredited = form.cleaned_data['is_accredited']

                        location.accreditation_agency = form.cleaned_data['accreditation_agency']

                    else:

                        location.is_accredited = organization.is_organization_accredited

                        location.accreditation_agency = organization.accreditation_agency

                    location.save()

                    organization.locations.add(location)

                elif location_already_in_db is True:

                    location = organization.locations.get(core_organization__id=organization.id, id=form.cleaned_data['id'])

                    location.hippa_notice_location = form.cleaned_data['hippa_notice_location']

                    location.emergency_location = form.cleaned_data['emergency_location']

                    if organization.is_electronic_postings_enabled.value == 1 and organization.is_electronic_postings_consistent.value == 0:

                        location.use_electronic_posting = form.cleaned_data['use_electronic_posting']

                    else:

                        location.use_electronic_posting = organization.is_electronic_postings_enabled


                    if organization.is_organization_accredited.value == 1 and organization.is_accredited_by_same_agency.value == 0:

                        location.is_accredited = form.cleaned_data['is_accredited']

                        location.accreditation_agency = form.cleaned_data['accreditation_agency']

                    else:

                        location.is_accredited = organization.is_accredited_by_same_agency

                        location.accreditation_agency = organization.accreditation_agency

                    location.save()

            return HttpResponseRedirect(reverse('admin_setup_location_2_3'))

        else:

            print 'validation failed'

    # if request is NOT post then lets load form simply
    else:

        formset = Location_2_2_Formset(initial=list_of_locations)

    # At the end we need to render the page and pass our form :)
    return render(request, 'admin/setup/location/location_2_2.html', {
        'formset': formset,
        'request': request,
        'organization': organization
    })


def location_2_3(request):

    organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

    total_active_locations_to_ask = organization.total_number_of_locations

    Location_2_3_Formset = formset_factory(Location_2_3, can_delete=False, can_order=False, max_num=total_active_locations_to_ask,  extra=total_active_locations_to_ask)

    list_of_locations = organization.locations.filter(core_organization__id=organization.id).order_by('id').values('id', 'short_name', 'no_of_fire_exists',  'where_written_hazard_located',  'when_hazard_prog_available',  'where_safety_data_located',  'eer_location', 'when_eer_available', 'emr_location', 'when_emr_available')

    # if request if POST then we need to process the form.
    if request.method == 'POST':

        formset = Location_2_3_Formset(request.POST)

        if formset.is_valid():

            for form in formset:

                print 'validation passed'

                location_already_in_db = organization.locations.filter(core_organization__id=organization.id, id=form.cleaned_data['id']).exists()

                if location_already_in_db is False:

                    location = CoreLocations()

                    location.no_of_fire_exists = form.cleaned_data['no_of_fire_exists']

                    location.eer_location = form.cleaned_data['eer_location']

                    location.when_eer_available = form.cleaned_data['when_eer_available']

                    location.emr_location = form.cleaned_data['emr_location']

                    location.when_emr_available = form.cleaned_data['when_emr_available']

                    location.where_written_hazard_located = form.cleaned_data['where_written_hazard_located']

                    location.when_hazard_prog_available = form.cleaned_data['when_hazard_prog_available']

                    location.where_safety_data_located = form.cleaned_data['where_safety_data_located']

                    location.save()

                    organization.locations.add(location)

                elif location_already_in_db is True:

                    location = organization.locations.get(core_organization__id=organization.id, id=form.cleaned_data['id'])

                    location.no_of_fire_exists = form.cleaned_data['no_of_fire_exists']

                    location.eer_location = form.cleaned_data['eer_location']

                    location.when_eer_available = form.cleaned_data['when_eer_available']

                    location.emr_location = form.cleaned_data['emr_location']

                    location.when_emr_available = form.cleaned_data['when_emr_available']


                    location.where_written_hazard_located = form.cleaned_data['where_written_hazard_located']

                    location.when_hazard_prog_available = form.cleaned_data['when_hazard_prog_available']

                    location.where_safety_data_located = form.cleaned_data['where_safety_data_located']

                    location.save()

            return HttpResponseRedirect(reverse('admin_setup_location_2_3_1'))

        else:

            print 'validation failed'

    # if request is NOT post then lets load form simply
    else:

        formset = Location_2_3_Formset(initial=list_of_locations)

    # At the end we need to render the page and pass our form :)
    return render(request, 'admin/setup/location/location_2_3.html', {
        'formset': formset,
        'request': request,
        'organization': organization
    })


def location_2_3_1(request):

    organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

    if organization.is_score_consistent.value == 1:

        list_of_locations = organization.locations.filter(core_organization__id=organization.id).order_by('id').values('id', 'short_name', 'min_score_general_knowledge',  'min_score_continuing_education', 'min_score_employee_competency', 'min_score_custom_courses')

        for location in list_of_locations:

            location = organization.locations.get(core_organization__id=organization.id, id=location['id'])

            location.min_score_general_knowledge = organization.min_score_general_knowledge

            location.min_score_continuing_education = organization.min_score_continuing_education

            location.min_score_employee_competency = organization.min_score_employee_competency

            location.min_score_custom_courses = organization.min_score_custom_courses

            location.save()

        return HttpResponseRedirect(reverse('admin_setup_location_2_3_2'))

    total_active_locations_to_ask = organization.total_number_of_locations

    Location_2_3_1_Formset = formset_factory(Location_2_3_1, can_delete=False, can_order=False, max_num=total_active_locations_to_ask,  extra=total_active_locations_to_ask)

    list_of_locations = organization.locations.filter(core_organization__id=organization.id).order_by('id').values('id', 'short_name', 'min_score_general_knowledge',  'min_score_continuing_education', 'min_score_employee_competency', 'min_score_custom_courses')

    # just setting the initial values similar to orgranization so user don't have to select all dropdowns
    for location in list_of_locations:

        location_new = organization.locations.get(core_organization__id=organization.id, id=location['id'])

        if location['min_score_general_knowledge'] is None:
            location_new.min_score_general_knowledge = organization.min_score_general_knowledge

        if location['min_score_continuing_education'] is None:
            location_new.min_score_continuing_education = organization.min_score_continuing_education

        if location['min_score_employee_competency'] is None:
            location_new.min_score_employee_competency = organization.min_score_employee_competency

        if location['min_score_employee_competency'] is None:
            location_new.min_score_custom_courses = organization.min_score_custom_courses

        location_new.save()

    # if request if POST then we need to process the form.
    if request.method == 'POST':

        formset = Location_2_3_1_Formset(request.POST)

        if formset.is_valid():

            for form in formset:

                print 'validation passed'

                location_already_in_db = organization.locations.filter(core_organization__id=organization.id, id=form.cleaned_data['id']).exists()

                if location_already_in_db is False:

                    location = CoreLocations()

                    location.min_score_general_knowledge = form.cleaned_data['min_score_general_knowledge']

                    location.min_score_continuing_education = form.cleaned_data['min_score_continuing_education']

                    location.min_score_employee_competency = form.cleaned_data['min_score_employee_competency']

                    location.min_score_custom_courses = form.cleaned_data['min_score_custom_courses']

                    location.save()

                    organization.locations.add(location)

                elif location_already_in_db is True:

                    location = organization.locations.get(core_organization__id=organization.id, id=form.cleaned_data['id'])

                    location.min_score_general_knowledge = form.cleaned_data['min_score_general_knowledge']

                    location.min_score_continuing_education = form.cleaned_data['min_score_continuing_education']

                    location.min_score_employee_competency = form.cleaned_data['min_score_employee_competency']

                    location.min_score_custom_courses = form.cleaned_data['min_score_custom_courses']

                    location.save()

            return HttpResponseRedirect(reverse('admin_setup_location_2_3_2'))

        else:

            print 'validation failed'

    # if request is NOT post then lets load form simply
    else:

        formset = Location_2_3_1_Formset(initial=list_of_locations)

    # At the end we need to render the page and pass our form :)
    return render(request, 'admin/setup/location/location_2_3_1.html', {
        'formset': formset,
        'request': request,
        'organization': organization
    })


def location_2_3_2(request):

    organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

    if organization.services_consistent.value == 1:

        list_of_locations = organization.locations.filter(core_organization__id=organization.id)

        list_of_services_offered = organization.services_offered.filter(core_organization__id=organization.id)

        for location in list_of_locations:

            # lets just clear ALL the exiting services from this location
            location.services_offered.clear()

            for service_offered in list_of_services_offered:

                location.services_offered.add(service_offered)

                location.save()

        return HttpResponseRedirect(reverse('admin_setup_location_2_3_3'))

    total_active_locations_to_ask = organization.total_number_of_locations

    Location_2_3_2_Formset = formset_factory(Location_2_3_2, can_delete=False, can_order=False, max_num=total_active_locations_to_ask,  extra=total_active_locations_to_ask)

    Location_2_3_2_Formset.form = staticmethod(curry(Location_2_3_2, organization=organization))

    list_of_locations = organization.locations.filter(core_organization__id=organization.id).order_by('id').values('id', 'short_name')

    # if request if POST then we need to process the form.
    if request.method == 'POST':

        formset = Location_2_3_2_Formset(request.POST)

        if formset.is_valid():

            for form in formset:

                print 'validation passed'

                location = organization.locations.get(core_organization__id=organization.id, id=form.cleaned_data['id'])

                location.services_offered.clear()

                for service_id in form.cleaned_data['services_offered']:

                    service_offered_already_in_db = location.services_offered.filter(id=service_id).exists()

                    if service_offered_already_in_db is False:

                        location.services_offered.add(service_id)

                        location.save()

            return HttpResponseRedirect(reverse('admin_setup_location_2_3_3'))

        else:

            print 'validation failed'

    # if request is NOT post then lets load form simply
    else:

        formset = Location_2_3_2_Formset(initial=list_of_locations)

    # At the end we need to render the page and pass our form :)
    return render(request, 'admin/setup/location/location_2_3_2.html', {
        'formset': formset,
        'request': request,
        'organization': organization
    })


def location_2_3_3(request):

    organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

    if organization.modules_consistent.value == 1:

        list_of_locations = organization.locations.filter(core_organization__id=organization.id)

        list_of_modules_offered = organization.modules.filter(core_organization__id=organization.id)

        for location in list_of_locations:

            # lets just clear ALL the exiting services from this location
            location.modules.clear()

            for module in list_of_modules_offered:

                location.modules.add(module)

                location.save()

        return HttpResponseRedirect(reverse('admin_setup_location_2_3_4'))

    total_active_locations_to_ask = organization.total_number_of_locations

    Location_2_3_3_Formset = formset_factory(Location_2_3_3, can_delete=False, can_order=False, max_num=total_active_locations_to_ask,  extra=total_active_locations_to_ask)

    Location_2_3_3_Formset.form = staticmethod(curry(Location_2_3_3, organization=organization))

    list_of_locations = organization.locations.filter(core_organization__id=organization.id).order_by('id').values('id', 'short_name')

    # if request if POST then we need to process the form.
    if request.method == 'POST':

        formset = Location_2_3_3_Formset(request.POST)

        if formset.is_valid():

            for form in formset:

                print 'validation passed'

                location = organization.locations.get(core_organization__id=organization.id, id=form.cleaned_data['id'])

                location.modules.clear()

                for module_id in form.cleaned_data['modules']:

                    module_already_in_db = location.modules.filter(id=module_id).exists()

                    if module_already_in_db is False:

                        location.modules.add(module_id)

                        location.save()

            return HttpResponseRedirect(reverse('admin_setup_location_2_3_4'))

        else:

            print 'validation failed'

    # if request is NOT post then lets load form simply
    else:

        formset = Location_2_3_3_Formset(initial=list_of_locations)

    # At the end we need to render the page and pass our form :)
    return render(request, 'admin/setup/location/location_2_3_3.html', {
        'formset': formset,
        'request': request,
        'organization': organization
    })


def location_2_3_4(request, location_number=0):

    organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

    total_non_organization_wide_officials = organization.officials.filter(is_organization_wide=0).count()

    if total_non_organization_wide_officials == 0 :
        return HttpResponseRedirect(reverse('admin_setup_department_3_1'))

    Location_2_3_4_Formset_Officials = formset_factory(Location_2_3_4_Officials, can_delete=False, can_order=False, max_num=1,  extra=1)

    list_of_locations = list(organization.locations.filter(core_organization__id=organization.id).order_by('id').values('id', 'short_name'))

    list_of_locations_int = organization.locations.filter(core_organization__id=organization.id).order_by('id').values('id', 'short_name').count()

    location_number_int = int(location_number)

    if location_number_int <= list_of_locations_int and location_number_int != 0:
        back_button_url = reverse('admin_setup_location_2_3_4_questions', args=(location_number_int-1,))

    if location_number_int == 0:
        back_button_url = reverse('admin_setup_location_2_3_3')

    # if request if POST then we need to process the form.
    if request.method == 'POST':

        form = Location_2_3_4(request.POST)

        formset_officials = Location_2_3_4_Formset_Officials(request.POST)

        if form.is_valid() and formset_officials.is_valid():

            print 'validation passed'

            location = organization.locations.get(core_organization__id=organization.id, id=form.cleaned_data['id'])

            for form_official in formset_officials:

                official_type = UtilOfficialTypes.objects.get(short_code=form_official.cleaned_data['short_code'])

                official_type_already_in_location = location.officials.filter(official_type_id=official_type.id).exists()

                if official_type_already_in_location == False:

                    official = CoreOfficials()

                    official.actual_job_title = form_official.cleaned_data['actual_job_title']

                    official.organization_job_title = form_official.cleaned_data['organization_job_title']

                    official.first_name = form_official.cleaned_data['first_name']

                    official.last_name = form_official.cleaned_data['last_name']

                    official.email = form_official.cleaned_data['email']

                    official.phone = form_official.cleaned_data['phone']

                    official.official_type = UtilOfficialTypes.objects.get(short_code=form_official.cleaned_data['short_code'])

                    official.is_organization_wide = 0

                    official.is_location_wide = form_official.cleaned_data['is_location_wide']

                    official.is_active = 1

                    official.save()

                    location.officials.add(official)

                    location.save()

                elif official_type_already_in_location == True:

                    official = location.officials.get(official_type_id=official_type.id)

                    official.actual_job_title = form_official.cleaned_data['actual_job_title']

                    official.organization_job_title = form_official.cleaned_data['organization_job_title']

                    official.first_name = form_official.cleaned_data['first_name']

                    official.last_name = form_official.cleaned_data['last_name']

                    official.email = form_official.cleaned_data['email']

                    official.phone = form_official.cleaned_data['phone']

                    official.official_type = UtilOfficialTypes.objects.get(short_code=form_official.cleaned_data['short_code'])

                    official.is_organization_wide = 0

                    official.is_location_wide = form_official.cleaned_data['is_location_wide']

                    official.is_active = 1

                    official.save()

            location_number_int = location_number_int+1

            if location_number_int < list_of_locations_int:

                return HttpResponseRedirect(reverse('admin_setup_location_2_3_4_questions', args=(location_number_int,)))

            if location_number_int == list_of_locations_int:

                return HttpResponseRedirect(reverse('admin_setup_department_3'))

        else:

            print 'validation failed'

    # if request is NOT post then lets load form simply
    else:

        selected_location = list_of_locations[location_number_int]

        list_of_non_org_officials = organization.officials.filter(is_organization_wide=0).values('id', 'organization_job_title', 'first_name', 'last_name', 'actual_job_title', 'email', 'phone', 'official_type_id')

        location = CoreLocations.objects.get(id=selected_location['id'])

        for official in list_of_non_org_officials:

            official_type_already_in_location = location.officials.filter(official_type_id=official['official_type_id']).exists()

            if official_type_already_in_location == True:

                print 'official_type_already_in_location==True'

            elif official_type_already_in_location == False:

                blank_official = CoreOfficials()

                blank_official.organization_job_title = official['organization_job_title']

                blank_official.first_name = official['first_name']

                blank_official.last_name = official['last_name']

                blank_official.actual_job_title = official['actual_job_title']

                blank_official.email = official['email']

                blank_official.phone = official['phone']

                blank_official.official_type_id = official['official_type_id']

                blank_official.save()

                location.officials.add(blank_official)

                location.save()

        form = Location_2_3_4(initial=selected_location)

        list_of_location_officials = location.officials.values('id', 'organization_job_title', 'first_name', 'last_name', 'actual_job_title', 'email', 'phone', 'official_type_id', 'is_location_wide')

        formset_officials = Location_2_3_4_Formset_Officials(initial=list_of_location_officials)


    # At the end we need to render the page and pass our form :)
    return render(request, 'admin/setup/location/location_2_3_4.html', {
        'form': form,
        'back_button_url': back_button_url,
        'formset_officials': formset_officials,
        'request': request,
        'organization': organization
    })
