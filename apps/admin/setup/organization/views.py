# Importing render module from django
from django.shortcuts import render

# this import will be used for redirection mainly
from django.core.urlresolvers import reverse

# Importing redirect module from django.
from django.http import HttpResponseRedirect

# now lets import all the forms from forms.py file in this app
# if forms are located somewhere else then we will need full path of app.
from forms import *


def organization_1_1(request):
	"""
	Every page calls it's own method so this method is called when user visits URL(admin/setup/organization_1_1)
	"""

	# if request if POST(means user have submitted form) then we need to process the form.
	if request.method == 'POST':
		# get all teh data form POST and sent it to form Organization_1_1
		form = Organization_1_1(request.POST)

		# lets check if form is actually valid or not?
		if form.is_valid():
			# if form is valid then start storing data.

			"""
			ORGANIZATION
			"""
			# first we need to get organization linked with this user. each user can be linked to one organization only.
			# now we have organization object.
			organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

			# Lets get the organization name and store it.
			organization.name = form.cleaned_data['org_name']

			# for all YES/NO fields we have a table and all model fields which have YES/NO answer are linked to that table via foreign key.
			# now we can't set ID to 1 OR 0 because it's incremental so we use column VALUE to hold 1 for YES and 0 for NO.
			# again every foreign key linked column will store OBJECT.
			organization.is_organization_accredited = UtilYesorNo.objects.get(value=form.data['is_organization_accredited'])

			# now we need to check few things here.....
			# we are using ".value" because that actually holds the value eof YES/NO. "organization.is_organization_accredited" is object.
			# If organization is accredited then we need to make sure that that we store values for other dependent fields.
			if organization.is_organization_accredited.value == 1:
				# foreign key with yes/no table and storing object for this field.
				organization.is_entire_organization_accredited = UtilYesorNo.objects.get(value=form.data['is_entire_organization_accredited'])

				# foreign key with yes/no table and storing object for this field.
				organization.is_accredited_by_same_agency = UtilYesorNo.objects.get(value=form.data['is_accredited_by_same_agency'])

				# foreign key with yes/no table and storing object for this field.
				organization.accreditation_agency = UtilRegAgencies.objects.get(id=form.data['accreditation_agency'])

			# if organization is NOT  accredited then just store NONE/NULL for all dependent fields.
			elif organization.is_organization_accredited.value == 0:
				# None means store Null -- we have specified in model that this field can have Null value, otherwise it will give error.
				organization.is_entire_organization_accredited = None

				# None means store Null -- we have specified in model that this field can have Null value, otherwise it will give error.
				organization.is_accredited_by_same_agency = None

				# None means store Null -- we have specified in model that this field can have Null value, otherwise it will give error.
				organization.accreditation_agency = None

			# Organization Type has foreign key with model "UtilOrganizationType" which holds all the organization types.
			# so we need to pass the type to get the object because this field stores OBJECT not VALUE.
			organization.entity_type = UtilOrganizationType.objects.get(id=form.cleaned_data['type'].id)

			# this step is IMPORTANT because we will lose all above values if we don't save organization object.
			# this will automatically store values in database.
			organization.save()

			"""
			LOCATION
			"""
			# check if organization already have locations... this will ONLY happen when user comes back to step 1.1 after adding multiple locations
			# in location setup section.  So we will get location from database and update the values instead of adding new entry.
			if organization.locations.count() > 0:
				existing_location = True

				# We need to get primary location of organization...In future setups user can add multiple organizations.
				# So if user gets back to this step then we just pull FIRST location that's why we use "[:1]" which gets just first result.
				# we also order it by ID because ID auto increments.
				# Address added here will be treated as FIRST location of organization and will be added to location tabel as well.
				location = organization.locations.filter(core_organization__id=organization.id).order_by('id')[:1].get()

			# this will be executed when user have no locations added yet, so we will create new location entry
			elif organization.locations.count() == 0:
				existing_location = False

				# just creating new model object from CoreLocations()
				location = CoreLocations()

			# this is fairly simple to understand...
			location.street_address_1 = form.cleaned_data['street_address_1']

			# this is fairly simple to understand...
			location.street_address_1 = form.cleaned_data['street_address_1']

			# this is fairly simple to understand...
			location.city = form.cleaned_data['city']

			# this is fairly simple to understand...
			location.state = form.cleaned_data['state']

			# this is fairly simple to understand...
			location.zip_code = form.cleaned_data['zip_code']

			# this is fairly simple to understand...
			location.phone = form.cleaned_data['phone']

			# this is fairly simple to understand...
			location.fax = form.cleaned_data['fax']

			# saving method will also be different if we are just updating existing location or adding new entry.
			if existing_location is True:
				# we also need to save location so that database entry is created for location as well.
				location.save()

			# this will be executed when user have no locations added yet, so we will create new location entry
			elif existing_location is False:
				# first we need to save location data
				location.save()

				# this will ADD new entry for location and we are using "organization.locations.add()" method because location has many-to-many relation with organization.
				organization.locations.add(location)

			"""
			POINT OF CONTACT
			"""
			# check if organization already have point_of_contacts... this will ONLY happen when user comes back to step 1.1 after adding multiple point_of_contacts
			# in point_of_contacts setup section.  So we will get point_of_contacts from database and update the values instead of adding new entry.
			if organization.point_of_contacts.count() > 0:
				# so user already have point_of_contacts so lets get it from database to update its values
				point_of_contact = organization.point_of_contacts.get(core_organization__id=organization.id)

			# this will be executed when user have no point_of_contacts added yet, so we will create new point_of_contacts entry
			elif organization.point_of_contacts.count() == 0:
				# just creating new model object from CorePointOfContacts()
				point_of_contact = CorePointOfContacts()

			# this is fairly simple to understand...
			point_of_contact.name = form.cleaned_data['point_of_contact_name']

			# this is fairly simple to understand...
			point_of_contact.title = form.cleaned_data['point_of_contact_title']

			# this is fairly simple to understand...
			point_of_contact.phone = form.cleaned_data['point_of_contact_phone']

			# this is fairly simple to understand...
			point_of_contact.email = form.cleaned_data['point_of_contact_email']

			# we also need to save point of contact so that database entry is created for point of contact as well.
			point_of_contact.save()

			# just for me debugging in console.....
			print 'validation passed'

			# so everything was good.. now redirect user to NEXT step.
			return HttpResponseRedirect(reverse('admin_setup_organization_1_2'))

		else:
			# just for me debugging in console.....
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		form = Organization_1_1()

		organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

		organization_locations = organization.locations.filter(core_organization__id=organization.id).order_by('id')[:1].get()

		organization_point_of_contact = organization.point_of_contacts.get(core_organization__id=organization.id)

		form.data['org_name'] = organization.name

		if organization.entity_type is None:
			form.data['type'] = ""
		elif organization.entity_type is not None:
			form.data['type'] = organization.entity_type.id

		form.data['street_address_1'] = organization_locations.street_address_1

		form.data['street_address_1'] = organization_locations.street_address_1

		form.data['city'] = organization_locations.city

		form.data['state'] = organization_locations.state

		form.data['zip_code'] = organization_locations.zip_code

		form.data['phone'] = organization_locations.phone

		form.data['fax'] = organization_locations.fax

		form.data['point_of_contact_name'] = organization_point_of_contact.name

		form.data['point_of_contact_title'] = organization_point_of_contact.title

		form.data['point_of_contact_phone'] = organization_point_of_contact.phone

		form.data['point_of_contact_email'] = organization_point_of_contact.email

		if organization.is_organization_accredited is None:
			form.data['is_organization_accredited'] = ""
		elif organization.is_organization_accredited is not None:
			form.data['is_organization_accredited'] = organization.is_organization_accredited.value

		if organization.is_entire_organization_accredited is None:
			form.data['is_entire_organization_accredited'] = ""
		elif organization.is_entire_organization_accredited is not None:
			form.data['is_entire_organization_accredited'] = organization.is_entire_organization_accredited.value

		if organization.is_accredited_by_same_agency is None:
			form.data['is_accredited_by_same_agency'] = ""
		elif organization.is_accredited_by_same_agency is not None:
			form.data['is_accredited_by_same_agency'] = organization.is_accredited_by_same_agency.value

		if organization.accreditation_agency is None:
			form.data['accreditation_agency'] = ""
		elif organization.accreditation_agency is not None:
			form.data['accreditation_agency'] = organization.accreditation_agency.id

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/organization/organization_1_1.html', {'form': form, 'request': request, })


def organization_1_2(request):
	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	monthly_safety_program = organization.billing.plan.modules.filter(short_code='monthly_safety_program_custom', is_active=True).exists()

	# if request if POST then we need to process the form.
	if request.method == 'POST':
		# get all teh data form POST to form  SignUpFormTerms
		form = Organization_1_2(request.POST, organization=organization)

		if form.is_valid():
			organization.is_score_consistent = UtilYesorNo.objects.get(value=form.data['is_score_consistent'])

			organization.min_score_general_knowledge = UtilPassingScores.objects.get(score=form.data['min_score_general_knowledge'])

			organization.min_score_continuing_education = UtilPassingScores.objects.get(score=form.data['min_score_continuing_education'])

			organization.min_score_employee_competency = UtilPassingScores.objects.get(score=form.data['min_score_employee_competency'])

			organization.min_score_custom_courses = UtilPassingScores.objects.get(score=form.data['min_score_custom_courses'])

			if monthly_safety_program is True:
				organization.is_signup_monthly_safety_program = UtilYesorNo.objects.get(value=form.data['is_signup_monthly_safety_program'])

				organization.is_course_selections_consistent = UtilYesorNo.objects.get(value=form.data['is_course_selections_consistent'])

			else:
				organization.is_signup_monthly_safety_program = None

				organization.is_course_selections_consistent = None

			print 'validation passed'

			organization.save()

			return HttpResponseRedirect(reverse('admin_setup_organization_1_3'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		form = Organization_1_2()

		organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

		if organization.is_score_consistent is None:
			form.data['is_score_consistent'] = CoreSettings.objects.get(short_code__exact='DEFAULT_is_score_consistent').value
		elif organization.is_score_consistent is not None:
			form.data['is_score_consistent'] = organization.is_score_consistent.value

		if organization.min_score_general_knowledge is None:
			form.data['min_score_general_knowledge'] = CoreSettings.objects.get(short_code__exact='DEFAULT_min_score_general_knowledge').value
		elif organization.min_score_general_knowledge is not None:
			form.data['min_score_general_knowledge'] = organization.min_score_general_knowledge.score

		if organization.min_score_continuing_education is None:
			form.data['min_score_continuing_education'] = CoreSettings.objects.get(short_code__exact='DEFAULT_min_score_continuing_education').value
		elif organization.min_score_continuing_education is not None:
			form.data['min_score_continuing_education'] = organization.min_score_continuing_education.score

		if organization.min_score_employee_competency is None:
			form.data['min_score_employee_competency'] = CoreSettings.objects.get(short_code__exact='DEFAULT_min_score_employee_competency').value
		elif organization.min_score_employee_competency is not None:
			form.data['min_score_employee_competency'] = organization.min_score_employee_competency.score

		if organization.min_score_custom_courses is None:
			form.data['min_score_custom_courses'] = CoreSettings.objects.get(short_code__exact='DEFAULT_min_score_custom_courses').value
		elif organization.min_score_custom_courses is not None:
			form.data['min_score_custom_courses'] = organization.min_score_custom_courses.score

		if monthly_safety_program is True:
			if organization.is_signup_monthly_safety_program is None:
				form.data['is_signup_monthly_safety_program'] = CoreSettings.objects.get(short_code__exact='DEFAULT_is_signup_monthly_safety_program').value
			elif organization.is_signup_monthly_safety_program is not None:
				form.data['is_signup_monthly_safety_program'] = organization.is_signup_monthly_safety_program.value

			if organization.is_course_selections_consistent is None:
				form.data['is_course_selections_consistent'] = CoreSettings.objects.get(short_code__exact='DEFAULT_is_course_selections_consistent').value
			elif organization.is_course_selections_consistent is not None:
				form.data['is_course_selections_consistent'] = organization.is_course_selections_consistent.value

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/organization/organization_1_2.html', {'form': form, 'request': request, 'organization': organization, 'monthly_safety_program': monthly_safety_program})


def organization_1_3(request):
	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	employee_sanction_monitoring = organization.billing.plan.modules.filter(short_code='employee_sanction_monitoring', is_active=True).exists()

	# if request if POST then we need to process the form.
	if request.method == 'POST':
		# get all teh data form POST to form  SignUpFormTerms
		form = Organization_1_3(request.POST, organization=organization)

		if form.is_valid():
			organization.is_electronic_postings_enabled = UtilYesorNo.objects.get(value=form.data['is_electronic_postings_enabled'])

			if form.data['is_electronic_postings_enabled'] == '1':
				organization.is_electronic_postings_consistent = UtilYesorNo.objects.get(value=form.data['is_electronic_postings_consistent'])
			else:
				organization.is_electronic_postings_consistent = UtilYesorNo.objects.get(value=0)

			if employee_sanction_monitoring is True:
				organization.is_use_ssn_for_user = UtilYesorNo.objects.get(value=form.data['is_use_ssn_for_user'])

			else:
				organization.is_use_ssn_for_user = None

			organization.total_number_of_employees = form.data['total_number_of_employees']

			organization.is_employee_specific_id = UtilYesorNo.objects.get(value=form.data['is_employee_specific_id'])

			organization.total_number_of_locations = form.data['total_number_of_locations']

			print 'validation passed'

			organization.save()

			return HttpResponseRedirect(reverse('admin_setup_organization_1_4'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		form = Organization_1_3()

		if organization.is_electronic_postings_enabled is None:
			form.data['is_electronic_postings_enabled'] = ""
		elif organization.is_electronic_postings_enabled is not None:
			form.data['is_electronic_postings_enabled'] = organization.is_electronic_postings_enabled.value

		if organization.is_electronic_postings_consistent is None:
			form.data['is_electronic_postings_consistent'] = ""
		elif organization.is_electronic_postings_consistent is not None:
			form.data['is_electronic_postings_consistent'] = organization.is_electronic_postings_consistent.value

		if employee_sanction_monitoring is True:
			if organization.is_use_ssn_for_user is None:
				form.data['is_use_ssn_for_user'] = ""
			elif organization.is_use_ssn_for_user is not None:
				form.data['is_use_ssn_for_user'] = organization.is_use_ssn_for_user.value

		if organization.total_number_of_employees is None:
			form.data['total_number_of_employees'] = ""
		elif organization.total_number_of_employees is not None:
			form.data['total_number_of_employees'] = organization.total_number_of_employees

		if organization.is_employee_specific_id is None:
			form.data['is_employee_specific_id'] = ""
		elif organization.is_employee_specific_id is not None:
			form.data['is_employee_specific_id'] = organization.is_employee_specific_id.value

		if organization.total_number_of_locations is None:
			form.data['total_number_of_locations'] = ""
		elif organization.total_number_of_locations is not None:
			form.data['total_number_of_locations'] = organization.total_number_of_locations

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/organization/organization_1_3.html', {'form': form, 'request': request, 'organization': organization, 'employee_sanction_monitoring': employee_sanction_monitoring})


def organization_1_4(request):
	core_settings = CoreSettings.objects.all()

	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	list_of_services_offered = CoreServicesOffered.objects.filter(is_active=True)

	# if request if POST then we need to process the form.
	if request.method == 'POST':
		# get all teh data form POST to form  SignUpFormTerms
		form = Organization_1_4(request.POST)

		if form.is_valid():
			organization.services_consistent = UtilYesorNo.objects.get(value=form.data['services_consistent_all_locations'])

			for field in form:
				if field.value() is True:
					organization.services_offered.add(CoreServicesOffered.objects.get(short_code__exact=field.name, is_active=True))

				elif field.value() is False:
					organization.services_offered.remove(CoreServicesOffered.objects.get(short_code__exact=field.name, is_active=True))

			print 'validation passed'

			organization.save()

			return HttpResponseRedirect(reverse('admin_setup_organization_1_5'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		form = Organization_1_4()

		if organization.is_score_consistent is None:
			form.data['services_consistent_all_locations'] = CoreSettings.objects.get(short_code__exact='DEFAULT_services_consistent').value
		elif organization.is_score_consistent is not None:
			form.data['services_consistent_all_locations'] = organization.services_consistent.value

		for service in organization.services_offered.filter(core_organization__id=organization.id):
			form.data[service.short_code] = True

			print 'normal load'

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/organization/organization_1_4.html', {'form': form, 'request': request, 'organization': organization})


def organization_1_5(request):
	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	list_of_available_modules = organization.billing.plan.modules.filter(is_active=True)

	#organization.modules.clear()

	#for module in list_of_available_modules:
	#	organization.modules.add(module)

	list_all_addon_modules = CoreModules.objects.filter(is_active=True, is_addon=True)

	# if request if POST then we need to process the form.
	if request.method == 'POST':
		# get all teh data form POST to form  SignUpFormTerms
		form = Organization_1_5(request.POST)

		if form.is_valid():
			organization.modules_consistent = UtilYesorNo.objects.get(value=form.data['modules_consistent'])

			print 'validation passed'

			organization.save()

			return HttpResponseRedirect(reverse('admin_setup_organization_1_7_questions', args=(1, 5)))
		#return HttpResponseRedirect(reverse('admin_setup_organization_1_6/1/5/'))

		else:
			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		form = Organization_1_5()

		if organization.modules_consistent is None:
			form.data['modules_consistent'] = CoreSettings.objects.get(short_code__exact='DEFAULT_modules_consistent').value
		elif organization.modules_consistent is not None:
			form.data['modules_consistent'] = organization.modules_consistent.value

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/organization/organization_1_5.html', {'form': form, 'request': request, 'organization': organization, 'list_all_addon_modules': list_all_addon_modules, 'list_of_available_modules': list_of_available_modules})

def organization_1_6(request):
	return render(request, 'admin/setup/organization/organization_1_6.html', {'request': request})

def organization_1_7(request, question_start=1, question_end=CoreSettings.objects.get(short_code__exact='DEFAULT_questions_per_page').value):
	global back_button_url

	organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)

	max_questions_to_display = int(question_end) - int(question_start)

	Organization_1_6_Formset = formset_factory(Organization_1_6, can_delete=False, can_order=False, max_num=max_questions_to_display)

	list_of_questions = UtilOfficialTypes.objects.filter(is_active=1, id__range=(question_start, question_end)).order_by('id').values('question', 'default_job_title', 'short_code')

	DEFAULT_questions_per_page = CoreSettings.objects.get(short_code__exact='DEFAULT_questions_per_page').value

	total_active_questions_to_ask = UtilOfficialTypes.objects.filter(is_active=1).count()

	# if request if POST then we need to process the form.
	if request.method == 'POST':
		formset = Organization_1_6_Formset(request.POST)

		if formset.is_valid():
			#organization.modules_consistent = UtilYesorNo.objects.get(value=form.data['modules_consistent'])
			for form in formset:
				print 'validation passed'

				official_to_get = UtilOfficialTypes.objects.get(is_active=1, short_code=form.cleaned_data['short_code'])

				official_already_in_db = organization.officials.filter(core_organization__id=organization.id, official_type=official_to_get.id).exists()

				if official_already_in_db is False:
					official = CoreOfficials()

					official.actual_job_title = form.cleaned_data['actual_job_title']

					official.organization_job_title = form.cleaned_data['organization_job_title']

					official.first_name = form.cleaned_data['first_name']

					official.last_name = form.cleaned_data['last_name']

					official.email = form.cleaned_data['email']

					official.phone = form.cleaned_data['phone']

					official.official_type = UtilOfficialTypes.objects.get(short_code=form.cleaned_data['short_code'])

					official.is_organization_wide = form.cleaned_data['is_organization_wide']

					official.is_active = 1

					official.save()

					organization.officials.add(official)

				elif official_already_in_db is True:
					official = organization.officials.get(core_organization__id=organization.id, official_type=official_to_get.id)

					official.actual_job_title = form.cleaned_data['actual_job_title']

					official.organization_job_title = form.cleaned_data['organization_job_title']

					official.first_name = form.cleaned_data['first_name']

					official.last_name = form.cleaned_data['last_name']

					official.email = form.cleaned_data['email']

					official.phone = form.cleaned_data['phone']

					official.official_type = UtilOfficialTypes.objects.get(short_code=form.cleaned_data['short_code'])

					#official.is_organization_wide = form.cleaned_data['is_organization_wide']
					official.is_organization_wide = form.cleaned_data['is_organization_wide']

					official.is_active = 1

					official.save()

			next_question_start = int(question_start) + int(DEFAULT_questions_per_page)

			next_question_end = int(question_end) + int(DEFAULT_questions_per_page)

			if next_question_end > total_active_questions_to_ask:
				next_question_end = int(total_active_questions_to_ask)

			if next_question_start > total_active_questions_to_ask:
				return HttpResponseRedirect(reverse('admin_setup_location_2_1'))

			else:
				return HttpResponseRedirect(reverse('admin_setup_organization_1_7_questions', args=(next_question_start, next_question_end)))
		else:
			global back_button_url

			back_question_start = int(question_start) - int(DEFAULT_questions_per_page)

			back_question_end = int(question_end) - int(DEFAULT_questions_per_page)

			if back_question_start < 1:
				back_button_url = reverse('admin_setup_organization_1_6')

			else:
				back_button_url = reverse('admin_setup_organization_1_7_questions', args=(back_question_start, back_question_end))

			print back_button_url

			print 'validation failed'

	# if request is NOT post then lets load form simply
	else:
		back_question_start = int(question_start) - int(DEFAULT_questions_per_page)

		back_question_end = int(question_end) - int(DEFAULT_questions_per_page)

		if back_question_start < 1:
			back_button_url = reverse('admin_setup_organization_1_6')

		else:
			back_button_url = reverse('admin_setup_organization_1_7_questions', args=(back_question_start, back_question_end))

		print back_button_url

		#for official in organization.officials.filter(core_organization__id=organization.id):

		#form.data[service.short_code] = True

		formset = Organization_1_6_Formset(initial=list_of_questions)

		for form in formset:
			official_to_get = UtilOfficialTypes.objects.get(is_active=1, short_code=form.initial['short_code'])

			official_already_in_db = organization.officials.filter(core_organization__id=organization.id, official_type=official_to_get.id).exists()

			if official_already_in_db is True:
				official = organization.officials.get(core_organization__id=organization.id, official_type=official_to_get.id)

				form.fields['organization_job_title'].widget.attrs['placeholder'] = form.initial['default_job_title']

				form.initial['organization_job_title'] = official.organization_job_title

				form.initial['first_name'] = official.first_name

				form.initial['last_name'] = official.last_name

				form.initial['actual_job_title'] = official.actual_job_title

				form.initial['email'] = official.email

				form.initial['phone'] = official.phone

				form.initial['is_organization_wide'] = official.is_organization_wide

			#form.initial['is_organization_wide'] = UtilYesorNo.objects.get(value=official.is_organization_wide.value)

			else:
				form.fields['organization_job_title'].widget.attrs['placeholder'] = form.initial['default_job_title']

	# At the end we need to render the page and pass our form :)
	return render(request, 'admin/setup/organization/organization_1_7.html', {'formset': formset, 'request': request, 'back_button_url': back_button_url, 'organization': organization})

