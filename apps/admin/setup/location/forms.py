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


class Location_2_1(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=True,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'placeholder': 'Location Name'}),
				     label='Location Name*')

	street_address_1 = forms.CharField(max_length=100, required=True,
					   validators=[custom_validator_valid_characters_space_with_and_sign],
					   widget=forms.TextInput(
						   attrs={'class': 'form-control', 'placeholder': 'Address 1'}),
					   label='Address 1*')

	street_address_2 = forms.CharField(max_length=100, required=False,
					   validators=[custom_validator_valid_characters_space_with_and_sign],
					   widget=forms.TextInput(
						   attrs={'class': 'form-control', 'placeholder': 'Address 2'}),
					   label='Address 2')

	city = forms.CharField(max_length=100, required=True, validators=[custom_validator_valid_characters_space],
			       widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
			       label='City*')

	state = CustomStateModelChoiceField(queryset=UtilUSAStates.objects.all(), required=True, to_field_name='name',
					    empty_label="Select State",
					    widget=forms.Select(
						    attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker',
							   'type': 'button'}), )

	zip_code = forms.CharField(max_length=100, required=True,
				   validators=[custom_validator_valid_characters_space_with_and_sign],
				   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip'}),
				   label='Zip*')

	phone = forms.CharField(max_length=100, required=True,
				validators=[custom_validator_valid_characters_space_with_and_sign],
				widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(xxx) xxx-xxxx'}),
				label='Direct Phone Number*')

	fax = forms.CharField(max_length=100, required=True,
			      validators=[custom_validator_valid_characters_space_with_and_sign],
			      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(xxx) xxx-xxxx'}),
			      label='Fax Number*')

	is_primary = CustomYesNoModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
						 label='Is this the main location?',
						 required=True, empty_label=None,
						 widget=forms.Select(
							 attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker',
								'type': 'button'}), )

	is_command_location = CustomYesNoModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
							  label='In a disaster situation, would this location be the command location?',
							  required=True, empty_label=None,
							  widget=forms.Select(
								  attrs={'class': 'select-block select-yes-no',
									 'id': 'selectpicker',
									 'type': 'button'}), )


class Location_2_2(forms.Form):
	def __init__(self, *args, **kwargs):
		self.organization = kwargs.pop('organization', None)
		super(Location_2_2, self).__init__(*args, **kwargs)

		organization = self.organization

		if organization.is_organization_accredited.value==1 and organization.is_accredited_by_same_agency.value==0:

			self.fields['is_accredited'] = CustomYesNoModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
										   label='Is this location accredited*',
										   required=True, empty_label=None,
										   widget=forms.Select(
											   attrs={'class': 'select-block select-yes-no',
												  'id': 'selectpicker',
												  'type': 'button'}), )

			self.fields['accreditation_agency'] = CustomYesNoModelChoiceField(
				queryset=UtilRegAgencies.objects.filter(subclassification_id='1', is_active='1'),
				label='Select Accrediting Agency*',
				required=False, empty_label='Accrediting Agency',
				widget=forms.Select(
					attrs={'class': 'select-block',
					       'id': 'selectpicker',
					       'type': 'button'}), )

		if organization.is_electronic_postings_enabled.value==1 and organization.is_electronic_postings_consistent.value==0:

			self.fields['use_electronic_posting'] = CustomYesNoModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
											    label='Use electronic postings feature for this location?',
											    required=True, empty_label=None,
											    widget=forms.Select(
												    attrs={'class': 'select-block select-yes-no',
													   'id': 'selectpicker',
													   'type': 'button'}), )

	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Location Name*')

	hippa_notice_location = forms.CharField(max_length=100, required=True,
						validators=[custom_validator_valid_characters_space_with_and_sign],
						widget=forms.TextInput(
							attrs={'class': 'form-control',
							       'placeholder': 'HIPAA Notice Location'}),
						label='Where at this location is the HIPAA Notice of Privacy Practices posted? (e.g, on the bulletin board in '
						      'the breakroom.)*')

	emergency_location = forms.CharField(max_length=100, required=True,
					     validators=[custom_validator_valid_characters_space_with_and_sign],
					     widget=forms.TextInput(
						     attrs={'class': 'form-control', 'placeholder': 'Refuge Location'}),
					     label='In an emergency, hazardous, or disaster situation, where should this location\'s employee gather to make '
						   'sure they are safe? (e.g., across the street at the flagpole.)*')


class Location_2_3(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Location Name*')

	no_of_fire_exists = forms.IntegerField(required=True,
					       validators=[custom_validator_valid_characters_space_with_and_sign],
					       widget=forms.TextInput(
						       attrs={'class': 'form-control',
							      'placeholder': 'Number of Fire Exits'}),
					       label='How many fire exits are at this location?')

	where_written_hazard_located = forms.CharField(max_length=256, required=True,
						       validators=[custom_validator_valid_characters_space_with_and_sign],
						       widget=forms.TextInput(
							       attrs={'class': 'form-control',
								      'placeholder': 'In the manager\'s office.'}),
						       label='Where is the written Hazard Communication program for this location? (e.g., In the manager\'s '
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
						    label='Where is the required list(s) of hazardous chemicals and safety data sheets for this location? (e.g'
							  '., In the manager\'s office.)')

	eer_location = forms.CharField(max_length=256, required=True,
				       validators=[custom_validator_valid_characters_space_with_and_sign],
				       widget=forms.TextInput(
					       attrs={'class': 'form-control',
						      'placeholder': 'Exposure Record Location'}),
				       label='Where are the Employee Exposure Records for this location kept? (e.g., in the Infection Control office.)')

	when_eer_available = forms.CharField(max_length=256, required=True,
					     validators=[custom_validator_valid_characters_space_with_and_sign],
					     widget=forms.TextInput(
						     attrs={'class': 'form-control', 'placeholder': 'Refuge Location'}),
					     label='When are these  Employee Exposure Records made available to employees? (e.g., Monday - Friday during '
						   'business hours.)')

	emr_location = forms.CharField(max_length=256, required=True,
				       validators=[custom_validator_valid_characters_space_with_and_sign],
				       widget=forms.TextInput(
					       attrs={'class': 'form-control', 'placeholder': 'Medical Record Location'}),
				       label='Where are the Employee Medical Records for this location kept? (e.g., in the Infection Control office.)')

	when_emr_available = forms.CharField(max_length=256, required=True,
					     validators=[custom_validator_valid_characters_space_with_and_sign],
					     widget=forms.TextInput(
						     attrs={'class': 'form-control', 'placeholder': 'Refuge Location'}),
					     label='When are these Employee Medical Records made available to employees? (e.g., Monday - Friday during '
						   'business hours.)')


class Location_2_3_1(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Location Name*')

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


class Location_2_3_2(forms.Form):
	"""
	    For admin_setup_organization_1_4
	    """

	def __init__(self, *args, **kwargs):

		self.organization = kwargs.pop('organization', None)

		super(Location_2_3_2, self).__init__(*args, **kwargs)

		services_offered = CoreServicesOffered.objects.filter(is_active=True).order_by('name').values_list('id', 'name')

		selected_values = {}

		if len(self.initial)!=0:
			location = self.organization.locations.get(id=self.initial['id'])

			services_offered_initials = location.services_offered.filter(is_active=True).order_by('name').values('id')

			for initial in services_offered_initials:

				selected_values[initial['id']] = initial['id']

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
				     label='Location Name*')


class Location_2_3_3(forms.Form):
	"""
	    For admin_setup_organization_1_4
	    """

	def __init__(self, *args, **kwargs):

		self.organization = kwargs.pop('organization', None)

		super(Location_2_3_3, self).__init__(*args, **kwargs)

		modules = CoreModules.objects.filter(is_active=True).order_by('name').values_list('id', 'name')

		selected_values = {}

		if len(self.initial)!=0:
			location = self.organization.locations.get(id=self.initial['id'])

			modules_initials = location.modules.filter(is_active=True).order_by('name').values('id')

			for initial in modules_initials:

				selected_values[initial['id']] = initial['id']

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
				     label='Location Name*')


class Location_2_3_4(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
				     validators=[custom_validator_valid_characters_space_with_and_sign],
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'readonly': ''}),
				     label='Location Name*')


class Location_2_3_4_Officials(forms.Form):
	def __init__(self, *args, **kwargs):

		super(Location_2_3_4_Officials, self).__init__(*args, **kwargs)

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

	YES_OR_NO = (
	(0, 'No'),
	(1, 'Yes'),
	)

	is_location_wide = forms.ChoiceField(required=True, choices=YES_OR_NO,
					     label='Applies to Entire Location*',
					     widget=forms.Select(attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker', 'type': 'button'}))



