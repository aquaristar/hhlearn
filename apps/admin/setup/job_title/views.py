# Importing render module from django
from django.shortcuts import render

# this import will be used for redirection mainly
from django.core.urlresolvers import reverse

# Importing redirect module from django.
from django.http import HttpResponseRedirect

from django.forms.formsets import formset_factory

from django.utils.functional import curry

# now lets import all the forms from forms.py file in this app
# if forms are located somewhere else then we will need full path of app.
from forms import *

# this is used for OR condition in .filter()
from django.db.models import Q


def job_title_5_1(request, show_all=0):
	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	back_button_url = reverse('admin_setup_region_4_1_questions', args=(organization.total_regions - 1,))

	if int(show_all)==0:

		show_all_url = reverse('admin_setup_job_title_5_1_questions', args=(1,))

		show_all_text = '[Show All]'

	elif int(show_all)==1:

		show_all_url = reverse('admin_setup_job_title_5_1_questions', args=(0,))

		show_all_text = '[Show Filter]'

	if request.method=='POST':
		# get all teh data form POST to form  SignUpFormTerms
		form = Job_Titles_5_1(request.POST, organization=organization, show_all=int(show_all))

		if form.is_valid():

			organization.job_titles.all().delete()

			for field in form:

				if field.value() is True:

					util_job_title = CoreJobTitles.objects.get(short_code=field.name)

					core_job_title = CoreJobTitles()

					core_job_title.short_code = util_job_title.short_code

					core_job_title.name = util_job_title.name

					core_job_title.name_possessive = util_job_title.name_possessive

					core_job_title.description = util_job_title.description

					core_job_title.category = util_job_title.category

					core_job_title.patient_file_access = util_job_title.patient_file_access

					core_job_title.exposure_to_chemicals = util_job_title.exposure_to_chemicals

					core_job_title.exposure_to_BBP = util_job_title.exposure_to_BBP

					core_job_title.exposure_to_TB = util_job_title.exposure_to_TB

					core_job_title.requires_license = util_job_title.requires_license

					core_job_title.cpr = util_job_title.cpr

					core_job_title.on_call = util_job_title.on_call

					core_job_title.flsa_status = util_job_title.flsa_status

					core_job_title.is_active = util_job_title.is_active

					core_job_title.save()

					organization.job_titles.add(core_job_title)

			print 'validation passed'

			organization.save()

			return HttpResponseRedirect(reverse('admin_setup_job_title_5_2'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		form = Job_Titles_5_1(organization=organization, show_all=int(show_all))

		services_offered = organization.services_offered.filter(is_active=True)

		if len(organization.job_titles.filter())==0:

			for service in services_offered:
				for job_title in service.job_titles.filter().order_by('name'):
					form.data[str(job_title.short_code)] = True

		elif len(organization.job_titles.filter()) > 0:

			for service in services_offered:
				for job_title in service.job_titles.filter().order_by('name'):

					job_title_exists = organization.job_titles.filter(Q(is_custom=0) | Q(is_custom=None), short_code=job_title.short_code).exists()

					if job_title_exists==True:

						form.data[str(job_title.short_code)] = True

					elif job_title_exists==False:

						form.data[str(job_title.short_code)] = False

			print 'normal load'

	return render(request, 'admin/setup/job_title/job_title_5_1.html',
	              {'request': request, 'form': form, 'back_button_url': back_button_url, 'show_all_url': show_all_url, 'show_all_text': show_all_text})


def job_title_5_2(request):
	back_button_url = reverse('admin_setup_job_title_5_1')

	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	total_job_tiles_for_org = organization.job_titles.filter(Q(is_custom=0) | Q(is_custom=None)).count()

	total_job_tiles_for_org_initials = organization.job_titles.filter(Q(is_custom=0) | Q(is_custom=None)).order_by('name').values('id', 'name', 'name_custom')

	Job_Titles_5_2_Formset = formset_factory(Job_Titles_5_2, can_delete=False, can_order=False, max_num=total_job_tiles_for_org, extra=total_job_tiles_for_org)

	if request.method=='POST':
		# get all teh data form POST to form  SignUpFormTerms
		formset = Job_Titles_5_2_Formset(request.POST)

		if formset.is_valid():

			for form in formset:

				if form.cleaned_data['name_custom']!=None:

					job_title = organization.job_titles.get(id=form.cleaned_data['id'])

					job_title.name_custom = form.cleaned_data['name_custom']

					if form.cleaned_data['name_custom'].endswith("s")==False and form.cleaned_data['name_custom']!="":

						job_title.name_custom_possessive = form.cleaned_data['name_custom'] + '\'s'

					elif form.cleaned_data['name_custom'].endswith("s")==True and form.cleaned_data['name_custom']!="":

						job_title.name_custom_possessive = form.cleaned_data['name_custom'] + '\''

					job_title.save()

			return HttpResponseRedirect(reverse('admin_setup_job_title_5_3'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		formset = Job_Titles_5_2_Formset(initial=total_job_tiles_for_org_initials)

		print 'normal load'

	return render(request, 'admin/setup/job_title/job_title_5_2.html',
	              {'request': request, 'formset': formset, 'back_button_url': back_button_url})


def job_title_5_3(request):
	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	back_button_url = reverse('admin_setup_job_title_5_2')

	# if request if POST then we need to process the form.
	if request.method=='POST':
		form = Job_Titles_5_3(request.POST, organization=organization)

		if form.is_valid():
			print 'validation passed'

			organization.custom_job_titles_enabled = form.cleaned_data['custom_job_titles_enabled']

			if organization.custom_job_titles_enabled.value==1:
				organization.total_custom_job_titles = form.cleaned_data['total_custom_job_titles']

			elif organization.custom_job_titles_enabled.value==0:
				organization.total_custom_job_titles = None

			organization.save()

			return HttpResponseRedirect(reverse('admin_setup_job_title_5_3_1'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		form = Job_Titles_5_3(organization=organization)

		form.fields['custom_job_titles_enabled'].initial = organization.custom_job_titles_enabled

		form.fields['total_custom_job_titles'].initial = organization.total_custom_job_titles

	return render(request, 'admin/setup/job_title/job_title_5_3.html', {'request': request, 'form': form, 'back_button_url': back_button_url})


def job_title_5_3_1(request):
	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	if organization.custom_job_titles_enabled.value==0:
		return HttpResponseRedirect(reverse('admin_setup_job_title_5_5'))

	back_button_url = reverse('admin_setup_job_title_5_3')

	total_custom_job_titles = organization.total_custom_job_titles

	if organization.job_titles.filter(is_custom=1).count()==0:

		for count in range(0, total_custom_job_titles):
			custom_job_title = CoreJobTitles()

			custom_job_title.is_custom = UtilYesorNo.objects.get(value=1)

			custom_job_title.job_category = UtilJobCategories.objects.get(short_code='custom')

			custom_job_title.save()

			organization.job_titles.add(custom_job_title)

	custom_job_tiles_for_org_initials = organization.job_titles.filter(is_custom=1).order_by('name').values('id', 'name', 'flsa_status', 'requires_license',
	                                                                                                        'cpr',
	                                                                                                        'on_call', 'patient_file_access',
	                                                                                                        'all_occupational_exposure',
	                                                                                                        'some_occupational_exposure',
	                                                                                                        'exposure_to_chemicals', 'exposure_to_TB')

	Job_Titles_5_3_1_Formset = formset_factory(Job_Titles_5_3_1, can_delete=False, can_order=False, max_num=total_custom_job_titles,
	                                           extra=total_custom_job_titles)

	Job_Titles_5_3_1_Formset.form = staticmethod(curry(Job_Titles_5_3_1, organization=organization))

	# if request if POST then we need to process the form.
	if request.method=='POST':

		formset = Job_Titles_5_3_1_Formset(request.POST)

		if formset.is_valid():

			for form in formset:

				print 'validation passed'

				job_title = organization.job_titles.get(id=form.cleaned_data['id'])

				job_title.name = form.cleaned_data['name']

				if form.cleaned_data['name'].endswith("s")==True:

					job_title.name_possessive = form.cleaned_data['name'] + '\''

				elif form.cleaned_data['name'].endswith("s")==False:
					job_title.name_possessive = form.cleaned_data['name'] + '\'s'

				job_title.short_code = form.cleaned_data['name'].lower().replace(" ", "_")

				job_title.flsa_status = form.cleaned_data['flsa_status']

				job_title.requires_license = form.cleaned_data['requires_license']

				job_title.cpr = form.cleaned_data['cpr']

				job_title.on_call = form.cleaned_data['on_call']

				job_title.patient_file_access = form.cleaned_data['patient_file_access']

				job_title.all_occupational_exposure = form.cleaned_data['all_occupational_exposure']

				job_title.some_occupational_exposure = form.cleaned_data['some_occupational_exposure']

				job_title.exposure_to_chemicals = form.cleaned_data['exposure_to_chemicals']

				job_title.exposure_to_TB = form.cleaned_data['exposure_to_TB']

				if form.cleaned_data['all_occupational_exposure'].value==1 or form.cleaned_data['some_occupational_exposure'].value==1:
					job_title.exposure_to_BBP = UtilYesorNo.objects.get(value=1)

				else:
					job_title.exposure_to_BBP = UtilYesorNo.objects.get(value=0)

				job_title.is_active = 1

				job_title.save()

			return HttpResponseRedirect(reverse('admin_setup_job_title_5_3_2'))

		else:

			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		formset = Job_Titles_5_3_1_Formset(initial=custom_job_tiles_for_org_initials)

		print 'normal load'

	return render(request, 'admin/setup/job_title/job_title_5_3_1.html',
	              {'request': request, 'formset': formset, 'back_button_url': back_button_url, 'organization': organization})


def job_title_5_3_2(request):
	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	if organization.locations.count() <= 1:

		return HttpResponseRedirect(reverse('admin_setup_job_title_5_4'))

	back_button_url = reverse('admin_setup_job_title_5_3_1')

	# if request if POST then we need to process the form.
	if request.method=='POST':

		form = Job_Titles_5_3_2(request.POST)

		if form.is_valid():

			print 'validation passed'

			organization.location_specific_job_titles = form.cleaned_data['location_specific_job_titles']

			organization.save()

			return HttpResponseRedirect(reverse('admin_setup_job_title_5_3_3'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		form = Job_Titles_5_3_2()

		form.fields['location_specific_job_titles'].initial = organization.location_specific_job_titles

	return render(

		request,

		'admin/setup/job_title/job_title_5_3_2.html',

		{
		'request': request,
		'form': form,
		'back_button_url': back_button_url
		}
	)


def job_title_5_3_3(request):
	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	if organization.location_specific_job_titles.value==0 or organization.locations.count() <= 1:

		return HttpResponseRedirect(reverse('admin_setup_job_title_5_4'))

	back_button_url = reverse('admin_setup_job_title_5_3_2')

	total_active_locations_to_ask = organization.total_number_of_locations

	Job_Titles_5_3_3_Formset = formset_factory(Job_Titles_5_3_3, can_delete=False, can_order=False, max_num=total_active_locations_to_ask,
	                                           extra=total_active_locations_to_ask)

	Job_Titles_5_3_3_Formset.form = staticmethod(curry(Job_Titles_5_3_3, organization=organization))

	list_of_locations = organization.locations.filter(core_organization__id=organization.id).order_by('id').values('id', 'short_name')


	# if request if POST then we need to process the form.
	if request.method=='POST':

		formset = Job_Titles_5_3_3_Formset(request.POST)

		if formset.is_valid():

			for form in formset:

				print 'validation passed'

				location = organization.locations.get(core_organization__id=organization.id, id=form.cleaned_data['id'])

				location.job_titles.clear()

				for job_title_id in form.cleaned_data['job_titles']:

					job_title_already_in_db = location.job_titles.filter(id=job_title_id).exists()

					if job_title_already_in_db is False:

						location.job_titles.add(job_title_id)

						location.save()

			return HttpResponseRedirect(reverse('admin_setup_job_title_5_3_4'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		formset = Job_Titles_5_3_3_Formset(initial=list_of_locations)

	return render(

		request,

		'admin/setup/job_title/job_title_5_3_3.html',

		{
		'request': request,
		'formset': formset,
		'back_button_url': back_button_url
		}
	)


def job_title_5_3_4(request):
	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	back_button_url = reverse('admin_setup_job_title_5_3_3')

	# if request if POST then we need to process the form.
	if request.method=='POST':

		form = Job_Titles_5_3_4(request.POST)

		if form.is_valid():

			print 'validation passed'

			organization.department_specific_job_titles = form.cleaned_data['department_specific_job_titles']

			organization.save()

			return HttpResponseRedirect(reverse('admin_setup_job_title_5_3_5'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		form = Job_Titles_5_3_4()

		form.fields['department_specific_job_titles'].initial = organization.department_specific_job_titles

	return render(

		request,

		'admin/setup/job_title/job_title_5_3_4.html',

		{
		'request': request,
		'form': form,
		'back_button_url': back_button_url
		}
	)


def job_title_5_3_5(request, location_number=0):

	back_button_url = ''

	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	if organization.department_specific_job_titles.value==0:
		return HttpResponseRedirect(reverse('admin_setup_job_title_5_4'))

	list_of_locations = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1, total_departments__gte=0).order_by('id').values('id', 'short_name')

	list_of_locations_int = list_of_locations.count()

	location_number_int = int(location_number)

	selected_location = list_of_locations[location_number_int]

	location = CoreLocations.objects.get(id=selected_location['id'])

	for department in location.departments.all():
		if department.job_titles.all().count() == 0:
			for job_title in location.job_titles.all():
				department.job_titles.add(job_title)

				department.save()

	total_departments_to_ask = location.total_departments

	Job_title_5_3_5_Formset = formset_factory(Job_title_5_3_5_JobTitles, can_delete=False, can_order=False, max_num=total_departments_to_ask,
                                          extra=total_departments_to_ask)

	Job_title_5_3_5_Formset.form = staticmethod(curry(Job_title_5_3_5_JobTitles, location=location))

	if location_number_int <= list_of_locations_int and location_number_int!=0:
		back_button_url = reverse('admin_setup_department_3_1_4_questions', args=(location_number_int - 1,))

	if location_number_int==0:
		list_of_locations_department_enabled = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by(
			'id').values('id', 'short_name')

		list_of_locations_department_enabled_int = list_of_locations_department_enabled.count()

		list_of_locations_department_enabled_int = int(list_of_locations_department_enabled_int)

		back_button_url = reverse('admin_setup_job_title_5_3_4')

	# if request if POST then we need to process the form.
	if request.method=='POST':

		formset = Job_title_5_3_5_Formset(request.POST)

		form = Job_title_5_3_5(request.POST)

		if form.is_valid() and formset.is_valid():
			for form in formset:
				print 'validation passed'

				department = CoreDepartments.objects.get(id=form.cleaned_data['id'])

				department.job_titles.clear()

				for job_title in form.cleaned_data['job_titles']:

					job_title_already_in_db = department.job_titles.filter(id=job_title).exists()

					if job_title_already_in_db is False:

						department.job_titles.add(job_title)

						department.save()

			location_number_int = location_number_int + 1

			if location_number_int < list_of_locations_int:
				return HttpResponseRedirect(reverse('admin_setup_job_title_5_3_5_questions', args=(location_number_int,)))

			if location_number_int==list_of_locations_int:
				return HttpResponseRedirect(reverse('admin_setup_job_title_5_4'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		selected_location = list_of_locations[location_number_int]

		form = Job_title_5_3_5(initial=selected_location)

		list_of_departments = location.departments.filter(is_active=1).order_by('id').values('id', 'short_name')

		formset = Job_title_5_3_5_Formset(initial=list_of_departments)

	return render(

		request,

		'admin/setup/job_title/job_title_5_3_5.html',

		{
		'request': request,
		'form': form,
		'formset': formset,
		'back_button_url': back_button_url
		}
	)


def job_title_5_4(request):

	back_button_url = ''

	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	list_of_locations_department_enabled = organization.locations.filter(core_organization__id=organization.id, departments_enabled_id=1).order_by(
		'id').values('id', 'short_name')

	list_of_locations_department_enabled_int = list_of_locations_department_enabled.count()

	list_of_locations_department_enabled_int = int(list_of_locations_department_enabled_int)

	back_button_url = reverse('admin_setup_job_title_5_3_5_questions', args=(list_of_locations_department_enabled_int - 1,))


	if organization.courses.filter(is_active=1).count() != CoreCourses.objects.filter(is_active=1).count():

		for course in CoreCourses.objects.filter(is_active=1):
			'''
			core_course = CoreCourses()

			core_course.core_course = CoreCourses()

			core_course.short_name = course.short_name

			core_course.name = course.name

			core_course.number = course.number

			core_course.description = course.description

			core_course.long_description = course.long_description

			core_course.type = course.type

			core_course.category = course.category

			#core_course.prerequisite = course.prerequisite

			core_course.regulatory_comments = course.regulatory_comments

			core_course.hours = course.hours

			core_course.continuing_education = course.continuing_education

			core_course.date_loaded = course.date_loaded

			core_course.date_last_updated = course.date_last_updated

			#core_course.number_of_pages = course.number_of_pages

			core_course.number_test_questions = course.number_test_questions

			core_course.has_referral_agencies = course.has_referral_agencies

			core_course.has_appendices = course.has_appendices

			core_course.has_glossary = course.has_glossary

			core_course.is_annual_course = course.is_annual_course

			core_course.monthly_safety_course = course.monthly_safety_course

			core_course.date_deactivated = course.date_deactivated

			core_course.date_deactivated = course.date_deactivated

			core_course.annual_start_date = course.annual_start_date

			core_course.annual_end_date = course.annual_end_date

			core_course.appendix = course.appendix

			core_course.is_custom = course.is_custom

			core_course.is_active = course.is_active

			core_course.save()

			organization.courses.add(core_course.id)
'''
			organization.courses.add(course.id)
	total_custom_job_titles_to_ask = organization.job_titles.filter(is_custom=1).count()

	Job_title_5_4_Formset = formset_factory(Job_title_5_4, can_delete=False, can_order=False, max_num=total_custom_job_titles_to_ask,
	                                        extra=total_custom_job_titles_to_ask)

	Job_title_5_4_Formset.form = staticmethod(curry(Job_title_5_4, organization=organization))

	list_of_custom_job_titles = organization.job_titles.filter(is_custom=1).order_by('id').values('id', 'name')
	# At the end we need to render the page and pass our form :)

	# if request if POST then we need to process the form.
	if request.method=='POST':

		formset = Job_title_5_4_Formset(request.POST)

		if formset.is_valid():

			for form in formset:

				print 'validation passed'

				custom_job_title = organization.job_titles.get(id=form.cleaned_data['id'], is_custom=1)

				custom_job_title.courses.clear()

				for course_id in form.cleaned_data['courses_offered']:

					course_offered_already_in_db = custom_job_title.courses.filter(id=course_id).exists()

					if course_offered_already_in_db is False:

						custom_job_title_course = JobTitleCoursesRelation(

							job_title=custom_job_title,

							course=organization.courses.get(id=course_id),

							number_of_days=None
						)

						custom_job_title_course.save()

			return HttpResponseRedirect(reverse('admin_setup_job_title_5_4_1'))

		else:

			print 'validation failed'

		# if request is NOT post then lets load form simply
	else:

		formset = Job_title_5_4_Formset(initial=list_of_custom_job_titles)

	return render(request, 'admin/setup/job_title/job_title_5_4.html', {
	'back_button_url': back_button_url,
	'formset': formset,
	'request': request,
	'organization': organization,
	'total_custom_job_titles_to_ask': total_custom_job_titles_to_ask
	})


def job_title_5_4_1(request, custom_job_title_number=0):

	back_button_url = reverse('admin_setup_job_title_5_4')

	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	list_custom_job_titles = organization.job_titles.filter(is_custom=1).order_by('id').values('id', 'name')

	list_custom_job_titles_int = list_custom_job_titles.count()

	custom_job_title_int = int(custom_job_title_number)

	selected_custom_job_title = list_custom_job_titles[custom_job_title_int]

	custom_job_title = CoreJobTitles.objects.get(id=selected_custom_job_title['id'])


	total_courses_to_ask = custom_job_title.courses.count()


	Job_title_5_4_1_Formset = formset_factory(Job_title_5_4_1_Courses, can_delete=False, can_order=False, max_num=total_courses_to_ask,
	                                          extra=total_courses_to_ask)

	Job_title_5_4_1_Formset.form = staticmethod(curry(Job_title_5_4_1_Courses, organization=organization))

	if custom_job_title_int <= list_custom_job_titles_int and custom_job_title_int!=0:
		back_button_url = reverse('admin_setup_job_title_5_4_1_questions', args=(custom_job_title_int - 1,))

	if custom_job_title_int == 0:

		back_button_url = reverse('admin_setup_job_title_5_4')

	# if request if POST then we need to process the form.
	if request.method == 'POST':

		formset = Job_title_5_4_1_Formset(request.POST)

		form = Job_title_5_4_1(request.POST)

		if form.is_valid() and formset.is_valid():


			for form_course in formset:

				print 'validation passed'

				custom_job_title_course = JobTitleCoursesRelation.objects.get(job_title=CoreJobTitles.objects.get(id=form.cleaned_data['id']), course=CoreCourses.objects.get(id=form_course.cleaned_data['id']))

				custom_job_title_course.number_of_days = form_course.cleaned_data['number_of_days']

				custom_job_title_course.save()

			custom_job_title_int = custom_job_title_int + 1

			if custom_job_title_int < list_custom_job_titles_int:
				return HttpResponseRedirect(reverse('admin_setup_job_title_5_4_1_questions', args=(custom_job_title_int,)))

			if custom_job_title_int==list_custom_job_titles_int:
				return HttpResponseRedirect(reverse('admin_setup_job_title_5_5'))

		else:

			print 'validation failed'

		# if request is NOT post then lets load form simply
	else:

		form = Job_title_5_4_1(initial=selected_custom_job_title)

		initial_values = {}

		index = 0

		for course in custom_job_title.courses.filter():

			custom_job_title_course = JobTitleCoursesRelation.objects.get(job_title=custom_job_title, course=course)

			initial_values[index] = {'id': custom_job_title_course.course.id, 'name': custom_job_title_course.course.name, 'number_of_days': custom_job_title_course.number_of_days}

			index += 1

		formset = Job_title_5_4_1_Formset(initial=initial_values)

	return render(request, 'admin/setup/job_title/job_title_5_4_1.html', {
	'back_button_url': back_button_url,
	'form': form,
	'formset': formset,
	'request': request,
	'organization': organization
	})


def job_title_5_4B(request):
	return render(request, 'admin/setup/job_title/job_title_5_4B.html', {'request': request})


def job_title_5_5(request):

	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	list_custom_job_titles_int = int(organization.job_titles.filter(is_custom=1).count())

	back_button_url = reverse('admin_setup_job_title_5_4_1_questions', args=(list_custom_job_titles_int - 1,))

	return render(request, 'admin/setup/job_title/job_title_5_5.html', {'request': request,'back_button_url': back_button_url})

