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


def department_3(request):
	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	list_of_locations_int = organization.locations.filter(core_organization__id=organization.id).order_by('id').count()

	back_button_url = reverse('admin_setup_location_2_3_4_questions', args=(list_of_locations_int - 1,))

	# if request if POST then we need to process the form.
	if request.method=='POST':
		form = Department_3(request.POST)

		if form.is_valid():
			print 'validation passed'

			organization.departments_enabled = form.cleaned_data['departments_enabled']

			organization.save()

			return HttpResponseRedirect(reverse('admin_setup_department_3_1'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		form = Department_3()

		form.fields['departments_enabled'].initial = organization.departments_enabled

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/department/department_3.html',
		      {'form': form, 'request': request, 'back_button_url': back_button_url, 'organization': organization})


def department_3_1(request):
	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	if organization.departments_enabled.value==0:
		return HttpResponseRedirect(reverse('admin_setup_region_4'))

	list_of_locations = organization.locations.filter(core_organization__id=organization.id).order_by('id').values('id', 'short_name',
														       'departments_enabled',
														       'total_departments')

	total_active_locations_to_ask = organization.total_number_of_locations

	Department_3_1_Formset = formset_factory(Department_3_1, can_delete=False, can_order=False, max_num=total_active_locations_to_ask,
						 extra=total_active_locations_to_ask)

	Department_3_1_Formset.form = staticmethod(curry(Department_3_1, organization=organization))

	# if request if POST then we need to process the form.
	if request.method=='POST':
		formset = Department_3_1_Formset(request.POST)

		if formset.is_valid():
			print 'validation passed'

			for form in formset:
				location = organization.locations.get(core_organization__id=organization.id, id=form.cleaned_data['id'])

				location.departments_enabled = form.cleaned_data['departments_enabled']

				location.total_departments = form.cleaned_data['total_departments']

				location.save()

			return HttpResponseRedirect(reverse('admin_setup_department_3_1_1'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		formset = Department_3_1_Formset(initial=list_of_locations)

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/department/department_3_1.html', {'formset': formset, 'request': request, 'organization': organization})


def department_3_1_1(request, location_number=0):
	back_button_url = ''

	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	if organization.departments_enabled.value==0:
		return HttpResponseRedirect(reverse('admin_setup_region_4'))

	list_of_locations = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by('id').values('id',
																		 'short_name')

	list_of_locations_int = list_of_locations.count()

	location_number_int = int(location_number)

	selected_location = list_of_locations[location_number_int]

	location = CoreLocations.objects.get(id=selected_location['id'])

	total_departments_to_ask = location.total_departments

	if location.departments.all().count()==0:
		for count in range(0, total_departments_to_ask):
			department = CoreDepartments()

			department.no_of_fire_exists = location.no_of_fire_exists

			department.emergency_location = location.emergency_location

			department.where_written_hazard_located = location.where_written_hazard_located

			department.when_hazard_prog_available = location.when_hazard_prog_available

			department.where_safety_data_located = location.where_safety_data_located

			department.hippa_notice_location = location.hippa_notice_location

			department.save()

			location.departments.add(department)

	Department_3_1_1_Formset = formset_factory(Department_3_1_1_Departments, can_delete=False, can_order=False, max_num=total_departments_to_ask,
						   extra=total_departments_to_ask)

	if location_number_int <= list_of_locations_int and location_number_int!=0:
		back_button_url = reverse('admin_setup_department_3_1_1_questions', args=(location_number_int - 1,))

	if location_number_int==0:
		back_button_url = reverse('admin_setup_department_3_1')

	# if request if POST then we need to process the form.
	if request.method=='POST':
		form = Department_3_1_1(request.POST)

		formset = Department_3_1_1_Formset(request.POST)

		if form.is_valid() and formset.is_valid():
			print 'validation passed'

			location = organization.locations.get(core_organization__id=organization.id, id=form.cleaned_data['id'])

			if location.departments.all().count() > 0:
				for department in location.departments.all():
					department.delete()

				location.departments.clear()

			for form_departments in formset:
				department = CoreDepartments()

				department.short_name = form_departments.cleaned_data['short_name']

				if organization.is_organization_accredited.value==1 and organization.is_accredited_by_same_agency.value==0:
					if location.is_accredited.value==1:
						department.is_accredited = form_departments.cleaned_data['is_accredited']
					else:
						department.is_accredited = None
				else:
					department.is_accredited = None

				if form_departments.cleaned_data['is_accredited'].value==1:
					department.accreditation_agency = form_departments.cleaned_data['accreditation_agency']
				else:
					department.accreditation_agency = None

				department.no_of_fire_exists = form_departments.cleaned_data['no_of_fire_exists']

				department.emergency_location = form_departments.cleaned_data['emergency_location']

				department.where_written_hazard_located = form_departments.cleaned_data['where_written_hazard_located']

				department.when_hazard_prog_available = form_departments.cleaned_data['when_hazard_prog_available']

				department.where_safety_data_located = form_departments.cleaned_data['where_safety_data_located']

				department.hippa_notice_location = form_departments.cleaned_data['hippa_notice_location']

				department.use_electronic_posting = form_departments.cleaned_data['use_electronic_posting']

				department.is_active = True

				department.save()

				location.departments.add(department)

			location_number_int = location_number_int + 1

			if location_number_int < list_of_locations_int:
				return HttpResponseRedirect(reverse('admin_setup_department_3_1_1_questions', args=(location_number_int,)))

			if location_number_int==list_of_locations_int:
				return HttpResponseRedirect(reverse('admin_setup_department_3_1_2'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		selected_location = list_of_locations[location_number_int]

		location = CoreLocations.objects.get(id=selected_location['id'])

		form = Department_3_1_1(initial=selected_location)

		list_of_departments = location.departments.order_by('id').values('id', 'short_name', 'is_accredited', 'accreditation_agency',
										 'where_written_hazard_located',  'when_hazard_prog_available',  'where_safety_data_located',
										 'no_of_fire_exists', 'emergency_location', 'hippa_notice_location',
										 'use_electronic_posting')

		formset = Department_3_1_1_Formset(initial=list_of_departments)

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/department/department_3_1_1.html',
		      {'form': form, 'formset': formset, 'request': request, 'location': location, 'back_button_url': back_button_url,
		       'organization': organization})


def department_3_1_2(request, location_number=0):
	back_button_url = ''

	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	if organization.departments_enabled.value==0:
		return HttpResponseRedirect(reverse('admin_setup_region_4'))

	if organization.is_score_consistent.value==1:
		list_of_locations = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by('id').values('id',
																			 'short_name',
																			 'min_score_general_knowledge',
																			 'min_score_continuing_education',
																			 'min_score_employee_competency',
																			 'min_score_custom_courses')

		for location in list_of_locations:
			for department in location.departments:
				department.min_score_general_knowledge = location.min_score_general_knowledge

				department.min_score_continuing_education = location.min_score_continuing_education

				department.min_score_employee_competency = location.min_score_employee_competency

				department.min_score_custom_courses = location.min_score_custom_courses

				department.save()

		return HttpResponseRedirect(reverse('admin_setup_department_3_1_3'))

	list_of_locations = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by('id').values('id',
																		 'short_name')

	list_of_locations_int = list_of_locations.count()

	location_number_int = int(location_number)

	selected_location = list_of_locations[location_number_int]

	location = CoreLocations.objects.get(id=selected_location['id'])

	total_departments_to_ask = location.total_departments

	Department_3_1_2_Formset = formset_factory(Department_3_1_2_Grading, can_delete=False, can_order=False, max_num=total_departments_to_ask,
						   extra=total_departments_to_ask)

	list_of_departments = location.departments.filter(is_active=1).order_by('id')

	# just setting the initial values similar to location so user don't have to select all dropdowns
	for department in list_of_departments:
		if department.min_score_general_knowledge is None:
			department.min_score_general_knowledge = location.min_score_general_knowledge

		if department.min_score_continuing_education is None:
			department.min_score_continuing_education = location.min_score_continuing_education

		if department.min_score_employee_competency is None:
			department.min_score_employee_competency = location.min_score_employee_competency

		if department.min_score_custom_courses is None:
			department.min_score_custom_courses = location.min_score_custom_courses

		department.save()

	if location_number_int <= list_of_locations_int and location_number_int!=0:
		back_button_url = reverse('admin_setup_department_3_1_2_questions', args=(location_number_int - 1,))

	if location_number_int==0:
		list_of_locations_department_enabled = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by(
			'id').values('id', 'short_name')

		list_of_locations_department_enabled_int = list_of_locations_department_enabled.count()

		list_of_locations_department_enabled_int = int(list_of_locations_department_enabled_int)

		back_button_url = reverse('admin_setup_department_3_1_1_questions', args=(list_of_locations_department_enabled_int - 1,))

	# if request if POST then we need to process the form.
	if request.method=='POST':
		formset = Department_3_1_2_Formset(request.POST)

		form = Department_3_1_2(request.POST)

		if form.is_valid() and formset.is_valid():
			for form in formset:
				print 'validation passed'

				department = CoreDepartments.objects.get(id=form.cleaned_data['id'])

				department.min_score_general_knowledge = form.cleaned_data['min_score_general_knowledge']

				department.min_score_continuing_education = form.cleaned_data['min_score_continuing_education']

				department.min_score_employee_competency = form.cleaned_data['min_score_employee_competency']

				department.min_score_custom_courses = form.cleaned_data['min_score_custom_courses']

				department.save()

			location_number_int = location_number_int + 1

			if location_number_int < list_of_locations_int:
				return HttpResponseRedirect(reverse('admin_setup_department_3_1_2_questions', args=(location_number_int,)))

			if location_number_int==list_of_locations_int:
				return HttpResponseRedirect(reverse('admin_setup_department_3_1_3'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		selected_location = list_of_locations[location_number_int]

		form = Department_3_1_2(initial=selected_location)

		list_of_departments = location.departments.filter(is_active=1).order_by('id').values('id', 'short_name', 'min_score_general_knowledge',
												     'min_score_continuing_education',
												     'min_score_employee_competency',
												     'min_score_custom_courses')

		formset = Department_3_1_2_Formset(initial=list_of_departments)

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/department/department_3_1_2.html',
		      {'form': form, 'formset': formset, 'request': request, 'back_button_url': back_button_url, 'organization': organization})


def department_3_1_3(request, location_number=0):
	back_button_url = ''

	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	if organization.departments_enabled.value==0:
		return HttpResponseRedirect(reverse('admin_setup_region_4'))

	if organization.modules_consistent.value==1:
		list_of_locations = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by('id').all()

		list_of_modules_offered = organization.modules.filter(core_organization__id=organization.id)

		for location in list_of_locations:
			for department in location.departments.all():
				# lets just clear ALL the exiting services from this location
				department.modules.clear()

				for module in list_of_modules_offered:
					department.modules.add(module)

					department.save()

		return HttpResponseRedirect(reverse('admin_setup_region_4'))

	list_of_locations = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by('id').values('id',
																		 'short_name')

	list_of_locations_int = list_of_locations.count()

	location_number_int = int(location_number)

	selected_location = list_of_locations[location_number_int]

	location = CoreLocations.objects.get(id=selected_location['id'])

	total_departments_to_ask = location.total_departments

	Department_3_1_3_Formset = formset_factory(Department_3_1_3_Modules, can_delete=False, can_order=False, max_num=total_departments_to_ask,
						   extra=total_departments_to_ask)

	Department_3_1_3_Formset.form = staticmethod(curry(Department_3_1_3_Modules, location=location))

	if location_number_int <= list_of_locations_int and location_number_int!=0:
		back_button_url = reverse('admin_setup_department_3_1_3_questions', args=(location_number_int - 1,))

	if location_number_int==0:
		list_of_locations_department_enabled = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by(
			'id').values('id', 'short_name')

		list_of_locations_department_enabled_int = list_of_locations_department_enabled.count()

		list_of_locations_department_enabled_int = int(list_of_locations_department_enabled_int)

		back_button_url = reverse('admin_setup_department_3_1_2_questions', args=(list_of_locations_department_enabled_int - 1,))

	# if request if POST then we need to process the form.
	if request.method=='POST':
		formset = Department_3_1_3_Formset(request.POST)

		form = Department_3_1_3(request.POST)

		if form.is_valid() and formset.is_valid():
			for form in formset:
				print 'validation passed'

				department = CoreDepartments.objects.get(id=form.cleaned_data['id'])

				department.modules.clear()

				for module in form.cleaned_data['modules']:
					module_already_in_db = department.modules.filter(id=module).exists()

					if module_already_in_db is False:
						department.modules.add(module)

						department.save()

			location_number_int = location_number_int + 1

			if location_number_int < list_of_locations_int:
				return HttpResponseRedirect(reverse('admin_setup_department_3_1_3_questions', args=(location_number_int,)))

			if location_number_int==list_of_locations_int:
				return HttpResponseRedirect(reverse('admin_setup_department_3_1_4'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		selected_location = list_of_locations[location_number_int]

		form = Department_3_1_3(initial=selected_location)

		list_of_departments = location.departments.filter(is_active=1).order_by('id').values('id', 'short_name')

		formset = Department_3_1_3_Formset(initial=list_of_departments)

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/department/department_3_1_3.html',
		      {'form': form, 'formset': formset, 'request': request, 'back_button_url': back_button_url, 'organization': organization})


def department_3_1_4(request, location_number=0):
	back_button_url = ''

	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	if organization.departments_enabled.value==0:
		return HttpResponseRedirect(reverse('admin_setup_region_4'))

	if organization.services_consistent.value==1:
		list_of_locations = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by('id').all()

		list_of_services_offered = organization.services_offered.filter(core_organization__id=organization.id)

		for location in list_of_locations:
			for department in location.departments.all():
				# lets just clear ALL the exiting services from this location
				department.services_offered.clear()

				for service in list_of_services_offered:
					department.services_offered.add(service)

					department.save()

		return HttpResponseRedirect(reverse('admin_setup_region_4'))

	list_of_locations = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by('id').values('id',
																		 'short_name')

	list_of_locations_int = list_of_locations.count()

	location_number_int = int(location_number)

	selected_location = list_of_locations[location_number_int]

	location = CoreLocations.objects.get(id=selected_location['id'])

	for department in location.departments.all():
		if department.services_offered.all().count()==0:
			for service in location.services_offered.all():
				department.services_offered.add(service)

				department.save()

	total_departments_to_ask = location.total_departments

	Department_3_1_4_Formset = formset_factory(Department_3_1_4_ServicesOffered, can_delete=False, can_order=False, max_num=total_departments_to_ask,
						   extra=total_departments_to_ask)

	Department_3_1_4_Formset.form = staticmethod(curry(Department_3_1_4_ServicesOffered, location=location))

	if location_number_int <= list_of_locations_int and location_number_int!=0:
		back_button_url = reverse('admin_setup_department_3_1_4_questions', args=(location_number_int - 1,))

	if location_number_int==0:
		list_of_locations_department_enabled = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by(
			'id').values('id', 'short_name')

		list_of_locations_department_enabled_int = list_of_locations_department_enabled.count()

		list_of_locations_department_enabled_int = int(list_of_locations_department_enabled_int)

		back_button_url = reverse('admin_setup_department_3_1_3_questions', args=(list_of_locations_department_enabled_int - 1,))

	# if request if POST then we need to process the form.
	if request.method=='POST':
		formset = Department_3_1_4_Formset(request.POST)

		form = Department_3_1_4(request.POST)

		if form.is_valid() and formset.is_valid():
			for form in formset:
				print 'validation passed'

				department = CoreDepartments.objects.get(id=form.cleaned_data['id'])

				department.services_offered.clear()

				for services in form.cleaned_data['services_offered']:
					service_already_in_db = department.services_offered.filter(id=services).exists()

					if service_already_in_db is False:
						department.services_offered.add(services)

						department.save()

			location_number_int = location_number_int + 1

			if location_number_int < list_of_locations_int:
				return HttpResponseRedirect(reverse('admin_setup_department_3_1_4_questions', args=(location_number_int,)))

			if location_number_int==list_of_locations_int:
				return HttpResponseRedirect(reverse('admin_setup_department_3_1_5'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		selected_location = list_of_locations[location_number_int]

		form = Department_3_1_4(initial=selected_location)

		list_of_departments = location.departments.filter(is_active=1).order_by('id').values('id', 'short_name')

		formset = Department_3_1_4_Formset(initial=list_of_departments)

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/department/department_3_1_4.html',
		      {'form': form, 'formset': formset, 'request': request, 'back_button_url': back_button_url, 'organization': organization})


def department_3_1_5(request, location_number=0, department_number=0):
	back_button_url = ''

	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	list_of_locations = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by('id').values('id',
																		 'short_name')

	list_of_locations_int = list_of_locations.count()

	location_number_int = int(location_number)

	selected_location = list_of_locations[location_number_int]

	location = CoreLocations.objects.get(id=selected_location['id'])

	department_number_int = int(department_number)

	list_of_departments = location.departments.filter(is_active=1).order_by('id').values('id', 'short_name')

	list_of_departments_int = list_of_departments.count()

	selected_department = list_of_departments[department_number_int]

	department = CoreDepartments.objects.get(id=selected_department['id'])

	total_non_location_wide_officials = location.officials.filter(is_location_wide=0).count()

	if total_non_location_wide_officials==0 or organization.departments_enabled.value==0:
		return HttpResponseRedirect(reverse('admin_setup_region_4'))

	if (location_number_int <= list_of_locations_int and location_number_int!=0) and (
			department_number_int <= list_of_departments_int and department_number_int!=0):
		back_button_url = reverse('admin_setup_department_3_1_5_questions', args=(location_number_int - 1, department_number_int - 1))

	if location_number_int==0:
		list_of_locations_department_enabled = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by(
			'id').values('id', 'short_name')

		list_of_locations_department_enabled_int = list_of_locations_department_enabled.count()

		list_of_locations_department_enabled_int = int(list_of_locations_department_enabled_int)

		back_button_url = reverse('admin_setup_department_3_1_4_questions', args=(list_of_locations_department_enabled_int - 1,))

	Department_3_1_5_Officials_Formset = formset_factory(Department_3_1_5_Officials, can_delete=False, can_order=False, max_num=1, extra=1)

	# if request if POST then we need to process the form.
	if request.method=='POST':
		form_department = Department_3_1_5_Department(request.POST)

		formset_officials = Department_3_1_5_Officials_Formset(request.POST)

		form = Department_3_1_5(request.POST)

		if form.is_valid() and form_department.is_valid() and formset_officials.is_valid():
			department = CoreDepartments.objects.get(id=form_department.cleaned_data['id'])

			for form_official in formset_officials:
				official_type = UtilOfficialTypes.objects.get(short_code=form_official.cleaned_data['short_code'])

				official_type_already_in_department = department.officials.filter(official_type_id=official_type.id).exists()

				if official_type_already_in_department==False:
					official = CoreOfficials()

					official.actual_job_title = form_official.cleaned_data['actual_job_title']

					official.organization_job_title = form_official.cleaned_data['organization_job_title']

					official.first_name = form_official.cleaned_data['first_name']

					official.last_name = form_official.cleaned_data['last_name']

					official.email = form_official.cleaned_data['email']

					official.phone = form_official.cleaned_data['phone']

					official.official_type = UtilOfficialTypes.objects.get(short_code=form_official.cleaned_data['short_code'])

					official.is_location_wide = None

					official.is_active = 1

					official.save()

					department.officials.add(official)

					department.save()

				elif official_type_already_in_department==True:
					official = department.officials.get(official_type_id=official_type.id)

					official.actual_job_title = form_official.cleaned_data['actual_job_title']

					official.organization_job_title = form_official.cleaned_data['organization_job_title']

					official.first_name = form_official.cleaned_data['first_name']

					official.last_name = form_official.cleaned_data['last_name']

					official.email = form_official.cleaned_data['email']

					official.phone = form_official.cleaned_data['phone']

					official.official_type = UtilOfficialTypes.objects.get(short_code=form_official.cleaned_data['short_code'])

					official.is_location_wide = None

					official.is_active = 1

					official.save()

			department_number_int = department_number_int + 1

			if department_number_int < list_of_departments_int:
				return HttpResponseRedirect(
					reverse('admin_setup_department_3_1_5_questions', args=(location_number_int, department_number_int)))

			if department_number_int==list_of_departments_int:
				location_number_int = location_number_int + 1

				if location_number_int < list_of_locations_int:
					department_number_int = 0
					return HttpResponseRedirect(
						reverse('admin_setup_department_3_1_5_questions', args=(location_number_int, department_number_int)))

				if location_number_int==list_of_locations_int:
					return HttpResponseRedirect(reverse('admin_setup_region_4'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		selected_location = list_of_locations[location_number_int]

		form = Department_3_1_5(initial=selected_location)

		form_department = Department_3_1_5_Department(initial=selected_department)

		if department.officials.all().count()==0:
			list_of_department_officials = location.officials.filter(is_location_wide=0).values('id', 'organization_job_title', 'first_name',
													    'last_name', 'actual_job_title', 'email', 'phone',
													    'official_type_id', 'is_location_wide')

		else:
			list_of_department_officials = department.officials.filter(is_active=1).values('id', 'organization_job_title', 'first_name',
												       'last_name', 'actual_job_title', 'email', 'phone',
												       'official_type_id', 'is_location_wide')

		formset_officials = Department_3_1_5_Officials_Formset(initial=list_of_department_officials)

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/department/department_3_1_5.html',
		      {'request': request, 'back_button_url': back_button_url, 'organization': organization, 'form_department': form_department,
		       'formset_officials': formset_officials, 'form': form})
