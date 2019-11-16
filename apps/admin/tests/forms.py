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


class TestForm(forms.Form):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(TestForm, self).__init__(*args, **kwargs)
		organization = self.user.core_user_profile.core_organization.get(user_profiles__id=self.user.core_user_profile.id)
		
		#add course titles field
		if organization.id == 1:
			t_course_ids = CoreTests.objects.all().values_list('course_id', flat=True)
			courses = CoreCourses.objects.all().exclude(id__in=t_course_ids)
		else:
			t_course_ids = CoreTests.objects.all().values_list('course_id', flat=True)
			course_ids = CoreOrganizationsCustomCourses.objects.filter(organizations_id=organization.id).values_list('courses_id', flat=True)
			courses = CoreCourses.objects.filter(id__in=course_ids).exclude(id__in=t_course_ids)
		
		self.fields['course']	= CustomYesNoModelChoiceField(queryset=courses,					    
							    required=True, empty_label=None,
							    widget=forms.Select(
								    attrs={'class': 'select-block select-yes-no',									   
									   'type': 'button'}), )
		#add test types field
		if organization.id == 1:
			types = CoreTestTypes.objects.all()
		else:
			types = CoreTestTypes.objects.filter(is_active=True)
		
		self.fields['type']	= CustomYesNoModelChoiceField(queryset=types,					    
							    required=True, empty_label=None,
							    widget=forms.Select(
								    attrs={'class': 'select-block select-yes-no',									   
									   'type': 'button'}), )
	questions_on_test = forms.IntegerField(widget=forms.HiddenInput(), label='', required=False)	
	is_active = forms.BooleanField(required=False,
							widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
							label='')
	