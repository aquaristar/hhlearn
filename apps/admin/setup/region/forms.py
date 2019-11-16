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


class Region_4(forms.Form):
	regions_enabled = CustomYesNoModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
						      label='Would you like to add Departments that are associated with specific Locations?*',
						      required=True, empty_label=None,
						      widget=forms.Select(
							      attrs={'class': 'select-block select-yes-no', 'id': 'selectpicker', 'type': 'button'}), )

	total_regions = forms.IntegerField(required=False,
					   validators=[custom_validator_valid_characters_space_with_and_sign],
					   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total Regions'}),
					   label='Total Regions*')

	def clean(self):

		cleaned_data = super(Region_4, self).clean()

		regions_enabled = cleaned_data.get("regions_enabled")

		total_regions = cleaned_data.get("total_regions")

		if regions_enabled.value==1 and total_regions is None:

			msg = u"Please specify the number of regions you want to add."
			self._errors["total_regions"] = self.error_class([msg])

		# Always return the full collection of cleaned data.
		return cleaned_data


class Region_4_1(forms.Form):

	def __init__(self, *args, **kwargs):

		self.organization = kwargs.pop('organization', None)

		super(Region_4_1, self).__init__(*args, **kwargs)

		selected_location_values = {}

		selected_department_values = {}


		locations = self.organization.locations.filter(is_active=True).order_by('short_name').values_list('id', 'short_name')

		location_list = self.organization.locations.filter(is_active=True, departments_enabled=True)

		departments = []

		for single_location in location_list:

			list_of_departments = list(single_location.departments.filter().order_by('short_name').values_list('id', 'short_name'))

			for department in list_of_departments:

				department_list = list(department)

				department_list[1] = department[1]+' / '+single_location.short_name

				department = tuple(department_list)

				departments.append(department)


		if len(self.initial)!=0:
			region = self.organization.regions.get(id=self.initial['id'])

			location_initials = region.locations.filter().order_by('short_name').values('id')

			for initial in location_initials:

				selected_location_values[initial['id']] = initial['id']




			department_initials = region.departments.filter().order_by('short_name').values('id')

			for initial in department_initials:

				selected_department_values[initial['id']] = initial['id']



		#for service in services_offered:
		self.fields['locations'] = forms.MultipleChoiceField(required=False,
									    choices=locations,
									    initial=selected_location_values,
									    widget=forms.SelectMultiple(
										    attrs={'class': 'form-control'}),
									    label='Select Locations')

		self.fields['departments'] = forms.MultipleChoiceField(required=False,
									    choices=departments,
									    initial=selected_department_values,
									    widget=forms.SelectMultiple(
										    attrs={'class': 'form-control'}),
									    label='Select Departments')

	id = forms.IntegerField(widget=forms.HiddenInput(), label='')

	short_name = forms.CharField(max_length=100, required=True,
			       validators=[custom_validator_valid_characters_space_with_and_sign],
			       widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Region Name'}),
			       label='Region Name*')


	def clean(self):

		cleaned_data = super(Region_4_1, self).clean()

		return cleaned_data


