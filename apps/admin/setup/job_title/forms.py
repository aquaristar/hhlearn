"""
All forms related to Organizational Setup are here.
"""

from validators import *

# Importing normal forms
from django import forms

from django.forms import ModelChoiceField

from apps.dashboard.models import *

from django.db.models import Q

from django.forms.formsets import formset_factory


class CustomStateModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.name


class CustomYesNoModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.name


class CustomPassingScoreModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.score


class Job_Titles_5_1(forms.Form):
	def __init__(self, *args, **kwargs):

		self.organization = kwargs.pop('organization', None)

		self.show_all = kwargs.pop('show_all', None)

		super(Job_Titles_5_1, self).__init__(*args, **kwargs)

		all_job_titles = ()

		if self.show_all==0:

			services_offered = self.organization.services_offered.filter(is_active=True).order_by('name')

			for service in services_offered:

				for job_title in service.job_titles.filter(is_active=True).order_by('name'):

					all_job_titles += ((job_title.short_code, job_title.name),)

			all_job_titles = sorted(all_job_titles, key=lambda name: name[1])   # sort by name

			for (short_code, name) in all_job_titles:
				self.fields['%s' % short_code] = forms.BooleanField(required=False, label=name)

		elif self.show_all==1:

			services_offered = CoreServicesOffered.objects.filter(is_active=True).order_by('name')

			for service in services_offered:

				job_titles = service.job_titles.filter(is_active=True).order_by('name')

				for job_title in job_titles:

					all_job_titles += ((job_title.short_code, job_title.name),)

			all_job_titles = sorted(all_job_titles, key=lambda name: name[1])   # sort by name

			for (short_code, name) in all_job_titles:
				self.fields['%s' % short_code] = forms.BooleanField(required=False, label=name)


class Job_Titles_5_2(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	name = forms.CharField(max_length=100, required=True,
	                       validators=[custom_validator_valid_characters_space_with_and_sign],
	                       widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'tabindex': "-1"}),
	                       label='Defailt Job Title')

	name_custom = forms.CharField(max_length=100, required=False,
	                              validators=[custom_validator_valid_characters_space_with_and_sign],
	                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Custom Job Title'}),
	                              label='Custom Job Title*')

	def clean(self):
		cleaned_data = super(Job_Titles_5_2, self).clean()

		# Always return the full collection of cleaned data.
		return cleaned_data


class Job_Titles_5_3(forms.Form):
	def __init__(self, *args, **kwargs):
		self.organization = kwargs.pop('organization', None)
		super(Job_Titles_5_3, self).__init__(*args, **kwargs)

	custom_job_titles_enabled = CustomYesNoModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
	                                                        label='Would you like to add any job titles into HHLEARN that were not on our list?*',
	                                                        required=True, empty_label=None,
	                                                        widget=forms.Select(
		                                                        attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker',
		                                                               'type': 'button'}), )

	total_custom_job_titles = forms.IntegerField(required=False,
	                                             validators=[custom_validator_valid_characters_space_with_and_sign],
	                                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total Job Titles'}),
	                                             label='Total Job Titles to Add*')

	def clean(self):

		cleaned_data = super(Job_Titles_5_3, self).clean()

		custom_job_titles_enabled = cleaned_data.get("custom_job_titles_enabled")

		total_custom_job_titles = cleaned_data.get("total_custom_job_titles")

		organization = self.organization

		if custom_job_titles_enabled.value==1 and total_custom_job_titles is None:

			msg = u"Please specify the number of job titles you want to add."
			self._errors["total_custom_job_titles"] = self.error_class([msg])

		if total_custom_job_titles < organization.total_custom_job_titles and custom_job_titles_enabled.value==1:
			msg = "You can\'t decrease total(" + str(
				organization.total_custom_job_titles) + ") number of custom job titles. However you can delete custom job titles after "\
			                                            "completing initial step."
			self._errors["total_custom_job_titles"] = self.error_class([msg])

		# Always return the full collection of cleaned data.
		return cleaned_data


class Job_Titles_5_3_1(forms.Form):
	def __init__(self, *args, **kwargs):
		self.organization = kwargs.pop('organization', None)

		super(Job_Titles_5_3_1, self).__init__(*args, **kwargs)

	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	name = forms.CharField(
		max_length=100, required=True,
		validators=[custom_validator_valid_characters_space_with_and_sign],
		widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder': 'Enter Your Job Titles*'
			}
		),
		label='Enter Your Job Titles*'
	)

	flsa_status = CustomYesNoModelChoiceField(
		queryset=UtilFlsaStatus.objects.all(),
		label='Is this job title "exempt" or "nonexempt" from overtime pay?',
		required=True, empty_label=None,
		widget=forms.Select(
			attrs={
			'class': 'select-block select-yes-no',
			'id': 'selectpicker',
			'type': 'button'
			}
		),
	)

	requires_license = CustomYesNoModelChoiceField(
		queryset=UtilYesorNo.objects.all(), to_field_name='value',
		label='Does this job title require any special license in order to perform this job?',
		required=True, empty_label=None,
		widget=forms.Select(
			attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker', 'type': 'button'}), )

	cpr = CustomYesNoModelChoiceField(
		queryset=UtilYesorNo.objects.all(), to_field_name='value',
		label='Does this job title require the individual to obtain and keep current a CPR certification?',
		required=True, empty_label=None,
		widget=forms.Select(
			attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker', 'type': 'button'}), )

	on_call = CustomYesNoModelChoiceField(
		queryset=UtilYesorNo.objects.all(), to_field_name='value',
		label='Does this job title have on-call duties?',
		required=True, empty_label=None,
		widget=forms.Select(
			attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker', 'type': 'button'}), )

	patient_file_access = CustomYesNoModelChoiceField(
		queryset=UtilYesorNo.objects.all(), to_field_name='value',
		label='Does this job title have access to patient medical files?',
		required=True, empty_label=None,
		widget=forms.Select(
			attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker', 'type': 'button'}), )

	all_occupational_exposure = CustomYesNoModelChoiceField(
		queryset=UtilYesorNo.objects.all(), to_field_name='value',
		label='Does <b>everyone</b> of the people with this job title have any reasonably anticipated '
		      'skin, '
		      'eye, mucous membrane, or parenteral contact with blood or other potentially infectious '
		      'materials '
		      'that may result from the performance of their duties?',
		required=True, empty_label=None,
		widget=forms.Select(
			attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker',
			       'type': 'button'}), )

	some_occupational_exposure = CustomYesNoModelChoiceField(
		queryset=UtilYesorNo.objects.all(), to_field_name='value',
		label='Do <b>some</b> of the people with this job title have any reasonably anticipated skin,'
		      ' eye, mucous membrane, or parenteral contact with blood or other potentially '
		      'infectious'
		      ' materials that may result from the performance of their duties?',
		required=True, empty_label=None,
		widget=forms.Select(
			attrs={
			'class': 'select-block select-yes-no',
			'id': 'selectpicker',
			'type': 'button'
			}
		),
	)

	exposure_to_chemicals = CustomYesNoModelChoiceField(
		queryset=UtilYesorNo.objects.all(), to_field_name='value',
		label='Does this job title have any contact with any hazardous chemicals?',
		required=True, empty_label=None,
		widget=forms.Select(
			attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker', 'type': 'button'}), )

	exposure_to_TB = CustomYesNoModelChoiceField(
		queryset=UtilYesorNo.objects.all(), to_field_name='value',
		label='Does this job title have any reasonably anticipated exposure to tuberculosis?',
		required=True, empty_label=None,
		widget=forms.Select(
			attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker', 'type': 'button'}), )

	def clean(self):
		cleaned_data = super(Job_Titles_5_3_1, self).clean()

		return cleaned_data


class Job_Titles_5_3_2(forms.Form):
	location_specific_job_titles = CustomYesNoModelChoiceField(
		queryset=UtilYesorNo.objects.all(),
		to_field_name='value',
		label='Would you like to limit job titles at the location level? This would mean that when a new employee is added to a location, they will be '
		      'restricted to selecting from the job titles you have specified for that location.',
		required=True,
		empty_label=None,
		widget=forms.Select(
			attrs={
			'class': 'select-block select-yes-no',
			'id': 'selectpicker',
			'type': 'button'
			}
		),
	)

	def clean(self):
		cleaned_data = super(Job_Titles_5_3_2, self).clean()

		# Always return the full collection of cleaned data.
		return cleaned_data


class Job_Titles_5_3_3(forms.Form):
	"""
	For admin_setup_organization_1_4
	"""

	def __init__(self, *args, **kwargs):

		self.organization = kwargs.pop('organization', None)

		super(Job_Titles_5_3_3, self).__init__(*args, **kwargs)

		job_titles = self.organization.job_titles.filter(is_active=True).order_by('name').values_list('id', 'name')

		selected_values = {}

		if len(self.initial) > 0:

			location = self.organization.locations.get(id=self.initial['id'])

			if location.job_titles.filter().count() > 0:

				job_titles_initials = location.job_titles.filter(is_active=True).order_by('name').values('id')

				for initial in job_titles_initials:

					selected_values[initial['id']] = initial['id']
			else:

				job_titles_initials = self.organization.job_titles.filter(is_active=True).order_by('name').values('id')

				for job_title in job_titles_initials:

					selected_values[job_title['id']] = job_title['id']



		#for service in services_offered:
		self.fields['job_titles'] = forms.MultipleChoiceField(
			required=False,
			choices=job_titles,
			initial=selected_values,
			widget=forms.SelectMultiple(
				attrs={
				'class': 'form-control'
				}
			),
			label='Available Job Titles'
		)

	id = forms.IntegerField(

		widget=forms.HiddenInput(),

		label=''
	)

	short_name = forms.CharField(

		max_length=100, required=False,

		validators=[custom_validator_valid_characters_space_with_and_sign],

		widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'readonly': ''
			}
		),

		label='Location Name*'
	)

	def clean(self):
		cleaned_data = super(Job_Titles_5_3_3, self).clean()

		# Always return the full collection of cleaned data.
		return cleaned_data


class Job_Titles_5_3_4(forms.Form):

	department_specific_job_titles = CustomYesNoModelChoiceField(
		queryset=UtilYesorNo.objects.all(),
		to_field_name='value',
		label='Would you like to limit job titles at the department level? This would mean that when a new employee is added to a location, they will be '
		      'restricted to selecting from the job titles you have specified for that department.',
		required=True,
		empty_label=None,
		widget=forms.Select(
			attrs={
			'class': 'select-block select-yes-no',
			'id': 'selectpicker',
			'type': 'button'
			}
		),
		)

	def clean(self):
		cleaned_data = super(Job_Titles_5_3_4, self).clean()

		# Always return the full collection of cleaned data.
		return cleaned_data



class Job_title_5_3_5(forms.Form):
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
	                             validators=[custom_validator_valid_characters_space_with_and_sign],
	                             widget=forms.TextInput(
		                             attrs={'class': 'form-control', 'readonly': ''}),
	                             label='Location Name*')

	def clean(self):

		cleaned_data = super(Job_title_5_3_5, self).clean()

		# Always return the full collection of cleaned data.
		return cleaned_data


class Job_title_5_3_5_JobTitles(forms.Form):
	def __init__(self, *args, **kwargs):

		self.location = kwargs.pop('location', None)

		super(Job_title_5_3_5_JobTitles, self).__init__(*args, **kwargs)

		job_titles = self.location.job_titles.filter(is_active=True).order_by('name').values_list('id', 'name')

		selected_values = {}


		if len(self.initial) > 0:

			department = self.location.departments.get(id=self.initial['id'])

			job_titles_initials = department.job_titles.filter(is_active=True).order_by('name').values('id')

			for job_title in job_titles_initials:

				selected_values[job_title['id']] = job_title['id']


		#for service in services_offered:
		self.fields['job_titles'] = forms.MultipleChoiceField(required=False,
		                                                            choices=job_titles,
		                                                            initial=selected_values,
		                                                            widget=forms.SelectMultiple(
			                                                            attrs={'class': 'form-control'}),
		                                                            label='Available Job Titles')

	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=False,
	                             validators=[custom_validator_valid_characters_space_with_and_sign],
	                             widget=forms.TextInput(
		                             attrs={'class': 'form-control', 'readonly': ''}),
	                             label='Department Name*')


	def clean(self):

		cleaned_data = super(Job_title_5_3_5_JobTitles, self).clean()

		# Always return the full collection of cleaned data.
		return cleaned_data



class Job_title_5_4(forms.Form):
	"""
	    For admin_setup_organization_1_4
	    """

	def __init__(self, *args, **kwargs):

		self.organization = kwargs.pop('organization', None)

		super(Job_title_5_4, self).__init__(*args, **kwargs)

		courses_available = self.organization.courses.filter(~Q(short_name='introduction_to_hhlearn'), is_active=1, monthly_safety_course_id=0).order_by(
			'name').values_list('id', 'name')

		selected_values = {}

		if len(self.initial) > 0:

			custom_job_title = self.organization.job_titles.get(id=self.initial['id'], is_custom=1)

			if custom_job_title.courses.filter().count() > 0:

				courses_offered_initials = custom_job_title.courses.filter(is_active=True).order_by('name').values('id')

				for initial in courses_offered_initials:

					selected_values[initial['id']] = initial['id']

			else:
				# monthly_safety_course_id =1 type courses are special and not offered on custom job titles.
				courses_offered_initials = self.organization.courses.filter(~Q(short_name='introduction_to_hhlearn'), is_active=1,
				                                                            monthly_safety_course_id=0).order_by('name').values('id')

				for initial in courses_offered_initials:

					selected_values[initial['id']] = initial['id']


		#for service in services_offered:
		self.fields['courses_offered'] = forms.MultipleChoiceField(required=False,
		                                                           choices=courses_available,
		                                                           initial=selected_values,
		                                                           widget=forms.SelectMultiple(
			                                                           attrs={'class': 'form-control'}),
		                                                           label='Available Courses')

	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	name = forms.CharField(max_length=100, required=False,
	                       validators=[custom_validator_valid_characters_space_with_and_sign],
	                       widget=forms.TextInput(
		                       attrs={'class': 'form-control', 'readonly': ''}),
	                       label='Custom Job Title')

	def clean(self):

		cleaned_data = super(Job_title_5_4, self).clean()

		# Always return the full collection of cleaned data.
		return cleaned_data


class Job_title_5_4_1(forms.Form):

	def __init__(self, *args, **kwargs):
		self.organization = kwargs.pop('organization', None)

		super(Job_title_5_4_1, self).__init__(*args, **kwargs)

	id = forms.IntegerField(
		widget=forms.HiddenInput(),
		label=''
	)

	name = forms.CharField(
		max_length=100,
		required=False,
		validators=[custom_validator_valid_characters_space_with_and_sign],
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'readonly': '',
				'tabindex':'-1'
			}
		),
		label='Custom Job Title'
	)

	def clean(self):
		cleaned_data = super(Job_title_5_4_1, self).clean()
		return cleaned_data


class Job_title_5_4_1_Courses(forms.Form):
	def __init__(self, *args, **kwargs):
		self.organization = kwargs.pop('organization', None)

		super(Job_title_5_4_1_Courses, self).__init__(*args, **kwargs)


	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	number_of_days = forms.IntegerField(label='Number of Days',  widget=forms.TextInput(
		attrs={'class': 'form-control',}))

	name = forms.CharField(max_length=100, required=False,
	                       validators=[custom_validator_valid_characters_space_with_and_sign],
	                       widget=forms.TextInput(
		                       attrs={'class': 'form-control', 'readonly': '', 'tabindex':'-1'}),
	                       label='Course Name')

	def clean(self):
		cleaned_data = super(Job_title_5_4_1_Courses, self).clean()

		# Always return the full collection of cleaned data.
		return cleaned_data
