"""
All forms related to Organizational Setup are here.
"""

from apps.admin.users.validators import *

# Importing normal forms
from django import forms

from django.forms import ModelChoiceField

from django.contrib.auth.models import Group


from django.core.validators	import *
from django.http import HttpResponseRedirect

from apps.dashboard.models import *


class CustomYesNoModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.name

class CustomLocationModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.short_name

class UserForm(forms.Form):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(UserInitialForm, self).__init__(*args, **kwargs)
		organization = self.user.core_user_profile.core_organization.get(user_profiles__id=self.user.core_user_profile.id)
		
		#add job_titles field
		job_titles = organization.job_titles.order_by('name').all()
		
		if len(job_titles) > 0:
			self.fields['job_title'] = CustomYesNoModelChoiceField(queryset=job_titles,					    
							    required=True, empty_label=None,
							    widget=forms.Select(
								    attrs={'class': 'select-block select-yes-no',
									   'id': 'selectpicker',
									   'type': 'button'}), )
			self.fields['job_title'].initial = self.user.core_user_profile.job_title_id
		
		#add locations field
		locations = organization.locations.order_by('short_name').all()
		
		if len(job_titles) > 0:
			self.fields['location'] = CustomLocationModelChoiceField(queryset=locations,					    
							    required=True, empty_label=None,
							    widget=forms.Select(
								    attrs={'class': 'select-block select-yes-no',
									   'id': 'selectpicker',
									   'type': 'button'}), )
			self.fields['location'].initial = self.user.core_user_profile.location_id
		
		if organization.is_employee_specific_id_id == 1:
			self.fields['employee_id'] = forms.CharField(max_length=100, required=True,
							 validators=[custom_validator_valid_characters_space_with_and_sign],
							 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID'}),
							 label='Employee ID')
			self.fields['employee_id'].initial = self.user.core_user_profile.organization_id_number
			
		if organization.is_use_ssn_for_user_id == 1:
			self.fields['social_security_number'] = forms.CharField(max_length=100, required=True,
							 validators=[custom_validator_valid_characters_space_with_and_sign],
							 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Social Security Number'}),
							 label='Social Security Number')
			self.fields['social_security_number'].initial = self.user.core_user_profile.user_social_security_number
			
	user_name = forms.CharField(max_length=100, required=True,				     
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'placeholder': 'User Name'}),
				     label='User Name')
	photo_file = forms.CharField(max_length=256, required=False,				     
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'type': 'photo', 'placeholder': 'photo'}),
				     label='photo')
			
	email = forms.EmailField(max_length=100, required=False,
							#validators=[custom_validator_unique_email],
				 			widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'disabled': 'disabled'}), label='Email Address')
	user_password = forms.CharField(max_length=100, required=True,				     
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Password'}),
				     label='Password')
	confirm_password = forms.CharField(max_length=100, required=True,				     
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Confirm Password'}),
				     label='Confirm Password')
	first_name = forms.CharField(max_length=100, required=False,				     
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'placeholder': 'First Name', 'disabled': 'disabled'}),
				     label='First Name')
	last_name = forms.CharField(max_length=100, required=False,				     
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'placeholder': 'Last Name', 'disabled': 'disabled'}),
				     label='Last Name')
	user_type = CustomYesNoModelChoiceField(queryset=Group.objects.all(),						    
						    empty_label=None,
						    required = False,
						    widget=forms.Select(
							    attrs={'class': 'select-block select-yes-no',
								   'id': 'selectpicker',
								   'disabled': 'disabled',
								   'style': 'background: #eee',
								   'type': 'button'}), )
		
	phone_work = forms.CharField(max_length=100, validators=[custom_validator_valid_phone_or_fax],
				widget=forms.TextInput(attrs={'class': 'form-control phone_number', 'placeholder': 'Home Phone Number'}),
				label='Home Phone Number')
	phone_alternate = forms.CharField(max_length=100, validators=[custom_validator_valid_phone_or_fax],
				widget=forms.TextInput(attrs={'class': 'form-control phone_number', 'placeholder': 'Alternate/Emergency Phone Number'}),
				label='Alternate/Emergency Phone Number')
	phone_oncall = forms.CharField(max_length=100, validators=[custom_validator_valid_phone_or_fax],
				widget=forms.TextInput(attrs={'class': 'form-control phone_number', 'placeholder': 'On-Call Phone Number'}),
				label='On-Call Phone Number')
	
class UserInitialForm(forms.Form):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(UserInitialForm, self).__init__(*args, **kwargs)
		organization = self.user.core_user_profile.core_organization.get(user_profiles__id=self.user.core_user_profile.id)
		
		#add job_titles field
		job_titles = organization.job_titles.order_by('name').all()
		
		if len(job_titles) > 0:
			self.fields['job_title'] = CustomYesNoModelChoiceField(queryset=job_titles,					    
							    required=True, empty_label=None,
							    widget=forms.Select(
								    attrs={'class': 'select-block select-yes-no',
									   'id': 'selectpicker',
									   'type': 'button'}), )
			self.fields['job_title'].initial = self.user.core_user_profile.job_title_id
		
		#add locations field
		locations = organization.locations.order_by('short_name').all()
		
		if len(job_titles) > 0:
			self.fields['location'] = CustomLocationModelChoiceField(queryset=locations,					    
							    required=True, empty_label=None,
							    widget=forms.Select(
								    attrs={'class': 'select-block select-yes-no',
									   'id': 'selectpicker',
									   'type': 'button'}), )
			self.fields['location'].initial = self.user.core_user_profile.location_id
		
		if organization.is_employee_specific_id_id == 1:
			self.fields['employee_id'] = forms.CharField(max_length=100, required=True,
							 validators=[custom_validator_valid_characters_space_with_and_sign],
							 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID'}),
							 label='Employee ID')
			self.fields['employee_id'].initial = self.user.core_user_profile.organization_id_number
			
		if organization.is_use_ssn_for_user_id == 1:
			self.fields['social_security_number'] = forms.CharField(max_length=100, required=True,
							 validators=[custom_validator_valid_characters_space_with_and_sign],
							 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Social Security Number'}),
							 label='Social Security Number')
			self.fields['social_security_number'].initial = self.user.core_user_profile.user_social_security_number
		
		self.fields['phone_oncall'].initial = self.user.core_user_profile.phone_oncall
		self.fields['phone_work'].initial = self.user.core_user_profile.phone_work
		self.fields['phone_alternate'].initial = self.user.core_user_profile.phone_alternate
		self.fields['photo_file'].initial = self.user.core_user_profile.photo_file
		self.fields['user_password'].initial = 'initial password'
	
	photo_file = forms.CharField(max_length=256, required=False,				     
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'type': 'photo', 'placeholder': 'photo'}),
				     label='photo')
			
	email = forms.EmailField(max_length=100, required=False,
							#validators=[custom_validator_unique_email],
				 			widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'disabled': 'disabled'}), label='Email Address')
	user_password = forms.CharField(max_length=100, required=False,				     
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Password', 'disabled': 'disabled'}),
				     label='Password')
	first_name = forms.CharField(max_length=100, required=False,				     
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'placeholder': 'First Name', 'disabled': 'disabled'}),
				     label='First Name')
	last_name = forms.CharField(max_length=100, required=False,				     
				     widget=forms.TextInput(
					     attrs={'class': 'form-control', 'placeholder': 'Last Name', 'disabled': 'disabled'}),
				     label='Last Name')
	user_type = CustomYesNoModelChoiceField(queryset=Group.objects.all(),						    
						    empty_label=None,
						    required = False,
						    widget=forms.Select(
							    attrs={'class': 'select-block select-yes-no',
								   'id': 'selectpicker',
								   'disabled': 'disabled',
								   'style': 'background: #eee',
								   'type': 'button'}), )
		
	phone_work = forms.CharField(max_length=100, validators=[custom_validator_valid_phone_or_fax],
				widget=forms.TextInput(attrs={'class': 'form-control phone_number', 'placeholder': 'Home Phone Number'}),
				label='Home Phone Number')
	phone_alternate = forms.CharField(max_length=100, validators=[custom_validator_valid_phone_or_fax],
				widget=forms.TextInput(attrs={'class': 'form-control phone_number', 'placeholder': 'Alternate/Emergency Phone Number'}),
				label='Alternate/Emergency Phone Number')
	phone_oncall = forms.CharField(max_length=100, validators=[custom_validator_valid_phone_or_fax],
				widget=forms.TextInput(attrs={'class': 'form-control phone_number', 'placeholder': 'On-Call Phone Number'}),
				label='On-Call Phone Number')
	

class UserModulesForm(forms.Form):
	'''def __init__(self, *args, **kwargs):
		self.module = kwargs.pop('module', None)
		super(UserModulesForm, self).__init__(*args, **kwargs)
	'''
	
	id = forms.IntegerField(widget=forms.HiddenInput(), label='')
	name = forms.CharField(widget=forms.HiddenInput(), label='')
	active_inactive = forms.BooleanField(required=False,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
'''
	def clean(self):

		cleaned_data = super(UserModulesForm, self).clean()
		is_active = cleaned_data.get("is_active")
		module = self.module
		module_name = self.module.name 
				
		return cleaned_data
	
	is_adding_custom_course = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
							
	is_external_benchmarking = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_internal_benchmarking = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_employee_handbook = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_employee_sanction_monitoring = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_forms_drm = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_forms_library = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_custom_forms_library = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_inservice_tracking = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_inservice_tracking_custom = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_messaging = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_monthly_safety_program = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_custom_monthly_safety_program = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_publications_drm = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_publications_library = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_custom_publications_library = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_verifed_messaging = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_videos_library = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	is_custom_videos_library = forms.BooleanField(required=True,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
							'''