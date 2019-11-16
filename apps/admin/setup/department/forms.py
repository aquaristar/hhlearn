"""
All forms related to Organizational Setup are here.
"""

from validators import *

# Importing normal forms
from django import forms

from django.forms import ModelChoiceField

from apps.dashboard.models import *


class CustomStateModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.name


class CustomYesNoModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.name


class CustomPassingScoreModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.score


class Department_3(forms.Form):
	departments_enabled = CustomYesNoModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
							  label='Would you like to add Departments that are associated with specific Locations?',
							  required=True, empty_label=None,
							  widget=forms.Select(
								  attrs={'class': 'select-block select-yes-no',
									 'id': 'selectpicker',
									 'type': 'button'}), )


class Department_3_1(forms.Form):
	def __init__(self, *args, **kwargs):
		self.organization = kwargs.pop('organization', None)
		super(Department_3_1, self).__init__(*args, **kwargs)

	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Location Name*')

	total_departments = forms.IntegerField(required=False,
					       validators=[custom_validator_valid_characters_space_with_and_sign],
					       widget=forms.TextInput(
						       attrs={'class': 'form-control', '': ''}),
					       label='Total Departments*')

	departments_enabled = CustomYesNoModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
							  label='Would you like to add Departments to this Location?*',
							  required=True, empty_label=None,
							  widget=forms.Select(
								  attrs={'class': 'select-block select-yes-no',
									 'id': 'selectpicker',
									 'type': 'button'}), )

	def clean(self):

		cleaned_data = super(Department_3_1, self).clean()

		departments_enabled = cleaned_data.get("departments_enabled")

		location_id = cleaned_data.get("id")

		total_departments = cleaned_data.get("total_departments")

		organization = self.organization

		location = organization.locations.get(core_organization__id=organization.id, id=location_id)

		if departments_enabled.value==1 and total_departments is None:
			# We know these are not in self._errors now (see discussion
			# below).
			msg = u"Please specify number of departments you want to add"
			self._errors["total_departments"] = self.error_class([msg])

		if total_departments < location.total_departments:
			msg = "You can\'t decrease total(" + str(
				location.total_departments) + ") number of department. However you can delete departments after completing initial step."
			self._errors["total_departments"] = self.error_class([msg])

		# Always return the full collection of cleaned data.
		return cleaned_data


class Department_3_1_1(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Location Name*')


class Department_3_1_1_Departments(forms.Form):
	short_name = forms.CharField(max_length=100, required=True,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'placeholder': 'Department Name'}),
				     label='Department Name*')

	is_accredited = CustomYesNoModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
						    label='Is department accredited?*',
						    required=False, empty_label=None,
						    widget=forms.Select(
							    attrs={'class': 'select-block select-yes-no',
								   'id': 'selectpicker',
								   'type': 'button'}), )

	accreditation_agency = CustomYesNoModelChoiceField(
		queryset=UtilRegAgencies.objects.filter(subclassification_id='1', is_active='1'),
		label='Select Accrediting Agency*',
		required=False, empty_label='Accrediting Agency',
		widget=forms.Select(
			attrs={'class': 'select-block',
			       'id': 'selectpicker',
			       'type': 'button'}), )

	no_of_fire_exists = forms.IntegerField(required=True,
					       validators=[custom_validator_valid_characters_space_with_and_sign],
					       widget=forms.TextInput(
						       attrs={'class': 'form-control',
							      'placeholder': 'Number of Fire Exits'}),
					       label='Number of Fire Exits*')


	where_written_hazard_located = forms.CharField(max_length=256, required=True,
						       validators=[custom_validator_valid_characters_space_with_and_sign],
						       widget=forms.TextInput(
							       attrs={'class': 'form-control',
								      'placeholder': 'In the manager\'s office.'}),
						       label='Where is the written Hazard Communication program for this department? (e.g., In the manager\'s '
							     'office.)')

	when_hazard_prog_available = forms.CharField(max_length=256, required=True,
						     validators=[custom_validator_valid_characters_space_with_and_sign],
						     widget=forms.TextInput(
							     attrs={'class': 'form-control',
								    'placeholder': 'Monday - Friday during business hours.'}),
						     label='When is the Hazard Communication program made available to employees? (e.g., Monday - Friday '
							   'during business hours.)')

	where_safety_data_located = forms.CharField(max_length=256, required=True,
						    validators=[custom_validator_valid_characters_space_with_and_sign],
						    widget=forms.TextInput(
							    attrs={'class': 'form-control',
								   'placeholder': 'In the manager\'s office.'}),
						    label='Where is the required list(s) of hazardous chemicals and safety data sheets for this department? (e.g'
							  '., In the manager\'s office.)')


	emergency_location = forms.CharField(max_length=256, required=True,
					     validators=[custom_validator_valid_characters_space_with_and_sign],
					     widget=forms.TextInput(
						     attrs={'class': 'form-control',
							    'placeholder': 'e.g., across the street at the flagpole.'}),
					     label='Emergency Refuge Location (e.g., across the street at the flagpole.)*')

	hippa_notice_location = forms.CharField(max_length=100, required=True,
						validators=[custom_validator_valid_characters_space_with_and_sign],
						widget=forms.TextInput(
							attrs={'class': 'form-control',
							       'placeholder': 'e.g, on the bulletin board in the breakroom'}),
						label='HIPAA Notice Placement (e.g, on the bulletin board in the breakroom.)*')

	use_electronic_posting = CustomYesNoModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
							     label='Use Electronic Postings*',
							     required=False, empty_label=None,
							     widget=forms.Select(
								     attrs={'class': 'select-block select-yes-no',
									    'id': 'selectpicker',
									    'type': 'button'}), )


class Department_3_1_2(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Location Name*')


class Department_3_1_2_Grading(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Department Name*')

	min_score_general_knowledge = CustomPassingScoreModelChoiceField(queryset=UtilPassingScores.objects.all(),
									 to_field_name='score', required=True, empty_label="Select Percentage",
									 label='General',
									 widget=forms.Select(
										 attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker',
											'type': 'button'}))

	min_score_continuing_education = CustomPassingScoreModelChoiceField(queryset=UtilPassingScores.objects.all(),
									    to_field_name='score', required=True,
									    empty_label="Select Percentage",
									    label='Continuing Education',
									    widget=forms.Select(
										    attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker',
											   'type': 'button'}))

	min_score_employee_competency = CustomPassingScoreModelChoiceField(queryset=UtilPassingScores.objects.all(),
									   to_field_name='score', required=True,
									   empty_label="Select Percentage",
									   label='Competency',
									   widget=forms.Select(
										   attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker',
											  'type': 'button'}))

	min_score_custom_courses = CustomPassingScoreModelChoiceField(queryset=UtilPassingScores.objects.all(), to_field_name='score',
								      required=True, empty_label="Select Percentage",
								      label='Custom Courses',
								      widget=forms.Select(
									      attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker',
										     'type': 'button'}))


class Department_3_1_3(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Location Name*')


class Department_3_1_3_Modules(forms.Form):
	def __init__(self, *args, **kwargs):

		self.location = kwargs.pop('location', None)

		super(Department_3_1_3_Modules, self).__init__(*args, **kwargs)

		modules = CoreModules.objects.filter(is_active=True).order_by('name').values_list('id', 'name')

		selected_values = {}

		if len(self.initial)!=0:
			department = self.location.departments.get(id=self.initial['id'])

			modules_initials = department.modules.filter(is_active=True).order_by('name').values('id')

			for module in modules_initials:

				selected_values[module['id']] = module['id']

		#for service in services_offered:
		self.fields['modules'] = forms.MultipleChoiceField(required=False,
								   choices=modules,
								   initial=selected_values,
								   widget=forms.SelectMultiple(
									   attrs={'class': 'form-control'}),
								   label='Available Modules')

	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Department Name*')


class Department_3_1_4(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Location Name*')


class Department_3_1_4_ServicesOffered(forms.Form):
	def __init__(self, *args, **kwargs):

		self.location = kwargs.pop('location', None)

		super(Department_3_1_4_ServicesOffered, self).__init__(*args, **kwargs)

		services_offered = CoreServicesOffered.objects.filter(is_active=True).order_by('name').values_list('id', 'name')

		selected_values = {}

		if len(self.initial)!=0:
			department = self.location.departments.get(id=self.initial['id'])

			services_initials = department.services_offered.filter(is_active=True).order_by('name').values('id')

			for service in services_initials:

				selected_values[service['id']] = service['id']

		#for service in services_offered:
		self.fields['services_offered'] = forms.MultipleChoiceField(required=False,
									    choices=services_offered,
									    initial=selected_values,
									    widget=forms.SelectMultiple(
										    attrs={'class': 'form-control'}),
									    label='Available Services')

	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Department Name*')


class Department_3_1_5(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Location Name*')


class Department_3_1_5_Department(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Department Name*')


class Department_3_1_5_Officials(forms.Form):
	def __init__(self, *args, **kwargs):

		super(Department_3_1_5_Officials, self).__init__(*args, **kwargs)

		if len(self.initial)!=0:
			official_type = UtilOfficialTypes.objects.get(id=self.initial['official_type_id'])

			self.fields['question'].initial = official_type.question

			self.fields['default_job_title'].initial = official_type.default_job_title

			self.fields['short_code'].initial = official_type.short_code

	question = forms.CharField(widget=forms.HiddenInput(), label='')

	default_job_title = forms.CharField(max_length=100, required=False,

					    widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': '', 'tabindex': '-1'}),
					    label='Default Job Title*')

	organization_job_title = forms.CharField(max_length=100, required=True,
						 validators=[custom_validator_valid_characters_space_with_and_sign],
						 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organization Job Title'}),
						 label='Organization Job Title*')

	first_name = forms.CharField(max_length=100, required=True, validators=[custom_validator_valid_characters_space],
				     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), label='First Name*')

	last_name = forms.CharField(max_length=100, required=True, validators=[custom_validator_valid_characters_space],
				    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), label='Last Name*')

	actual_job_title = forms.CharField(max_length=100, required=True,
					   validators=[custom_validator_valid_characters_space_with_and_sign],
					   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact\'s Actual Job Title'}),
					   label='Contact\'s Actual Job Title*')

	email = forms.EmailField(max_length=100, required=True,
				 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), label='Email Address*')

	phone = forms.CharField(max_length=100, required=True, validators=[custom_validator_valid_phone_or_fax],
				widget=forms.TextInput(attrs={'class': 'form-control phone_number', 'placeholder': '(xxx) xxx-xxxx'}),
				label='Direct Phone Number*')

	short_code = forms.CharField(widget=forms.HiddenInput(), label='')

	"""
	    YES_OR_NO = (
		(0, 'No'),
		(1, 'Yes'),
	    )

	    is_location_wide = forms.ChoiceField(required=True, choices=YES_OR_NO,
						 label='Applies to Entire Location*', widget=forms.Select(attrs={'class': 'select-block select-yes-no',
						 'id':'selectpicker', 'type':'button'}))
	    """



