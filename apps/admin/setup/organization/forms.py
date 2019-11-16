"""
All forms related to Organizational Setup are here.
"""

from validators import *

# Importing normal forms
from django import forms

from django.forms.formsets import formset_factory

from apps.utility.models import *


# Importing User model from django auth because we are using django builtin authentication syste.
from django.contrib.auth.models import User

from apps.dashboard.models import *



class Organization_1_1(forms.Form):
    """
    RegisterForm handles all the main registration process and performs all the validations etc.
    """

    org_name = forms.CharField(max_length=256, validators=[custom_validator_valid_characters_space])

    state = forms.ModelChoiceField(queryset=UtilUSAStates.objects.all(), required=True,  to_field_name='name', empty_label="(Nothing)")

    street_address_1 = forms.CharField(max_length=100, validators=[custom_validator_valid_characters_space])

    street_address_2 = forms.CharField(max_length=100, required=False,
                                       validators=[custom_validator_valid_characters_space])

    city = forms.CharField(max_length=100, validators=[custom_validator_valid_characters])

    zip_code = forms.CharField(max_length=6, validators=[custom_validator_valid_zip])

    type = forms.ModelChoiceField(queryset=UtilOrganizationType.objects.all(), required=True, empty_label="(Nothing)")

    phone = forms.CharField(max_length=100, validators=[custom_validator_valid_phone_or_fax])

    fax = forms.CharField(max_length=100, validators=[custom_validator_valid_phone_or_fax])

    point_of_contact_name = forms.CharField(max_length=100, required=True,
                                            validators=[custom_validator_valid_characters_space])

    point_of_contact_title = forms.CharField(max_length=100, required=True,
                                             validators=[custom_validator_valid_characters_space])

    point_of_contact_phone = forms.CharField(max_length=100, required=True,
                                             validators=[custom_validator_valid_phone_or_fax])

    point_of_contact_email = forms.EmailField(max_length=100, required=True)

    is_organization_accredited = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
                                                        required=True, empty_label="(Nothing)")

    is_entire_organization_accredited = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(),
                                                               to_field_name='value', empty_label="(Nothing)")

    is_accredited_by_same_agency = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
                                                          empty_label="(Nothing)")

    accreditation_agency = forms.ModelChoiceField(
        queryset=UtilRegAgencies.objects.filter(subclassification_id='1', is_active='1'), required=False,
        empty_label="(Nothing)")

    def clean(self):
        """
        This clean() method is executed automatically to check fields and I'm using it here to compare
        passwords.
        """
        cleaned_data = super(Organization_1_1, self).clean()

        is_organization_accredited = cleaned_data.get("is_organization_accredited")

        accreditation_agency = cleaned_data.get("accreditation_agency")

        if is_organization_accredited.value == 1 and accreditation_agency is None:
            # We know these are not in self._errors now (see discussion
            # below).
            msg = u"Please select accreditation agency."
            self._errors["accreditation_agency"] = self.error_class([msg])

            # These fields are no longer valid. Remove them from the
            # cleaned data.
            #del cleaned_data["accreditation_agency"]

        elif is_organization_accredited.value == 0:
            # These fields are no longer valid. Remove them from the
            # cleaned data.
            print("organization is not accredited.")
            #del cleaned_data["accreditation_agency"]

        # Always return the full collection of cleaned data.
        return cleaned_data


class Organization_1_2(forms.Form):
    """
    For admin_setup_organization_1_2
    """

    def __init__(self, *args, **kwargs):
        self.organization = kwargs.pop('organization', None)
        super(Organization_1_2, self).__init__(*args, **kwargs)

    is_score_consistent = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
                                                 required=True, empty_label="(Nothing)")

    min_score_general_knowledge = forms.ModelChoiceField(queryset=UtilPassingScores.objects.all(),
                                                         to_field_name='score', required=True, empty_label="(Nothing)")

    min_score_continuing_education = forms.ModelChoiceField(queryset=UtilPassingScores.objects.all(),
                                                            to_field_name='score', required=True,
                                                            empty_label="(Nothing)")

    min_score_employee_competency = forms.ModelChoiceField(queryset=UtilPassingScores.objects.all(),
                                                           to_field_name='score', required=True,
                                                           empty_label="(Nothing)")

    min_score_custom_courses = forms.ModelChoiceField(queryset=UtilPassingScores.objects.all(), to_field_name='score',
                                                      required=True, empty_label="(Nothing)")

    is_signup_monthly_safety_program = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
                                                              required=False, empty_label="(Nothing)")

    is_course_selections_consistent = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
                                                             required=False, empty_label="(Nothing)")

    def clean(self):

        cleaned_data = super(Organization_1_2, self).clean()

        is_signup_monthly_safety_program = cleaned_data.get("is_signup_monthly_safety_program")

        is_course_selections_consistent = cleaned_data.get("is_course_selections_consistent")

        organization = self.organization

        monthly_safety_program = organization.billing.plan.modules.filter(short_code='monthly_safety_program_custom',
                                                                           is_active=True).exists()

        if monthly_safety_program is True:

            if is_signup_monthly_safety_program is None or is_course_selections_consistent is None:
                raise forms.ValidationError('Provide either a date and time or a timestamp')
            else:
                return cleaned_data


class Organization_1_3(forms.Form):
    """
    For admin_setup_organization_1_3
    """

    def __init__(self, *args, **kwargs):
        self.organization = kwargs.pop('organization', None)
        super(Organization_1_3, self).__init__(*args, **kwargs)

    is_electronic_postings_enabled = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
                                                            required=True, empty_label="(Nothing)")

    is_electronic_postings_consistent = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(),
                                                               to_field_name='value', required=True,
                                                               empty_label="(Nothing)")

    is_use_ssn_for_user = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
                                                 required=False, empty_label="(Nothing)")

    total_number_of_employees = forms.IntegerField(required=True)

    is_employee_specific_id = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
                                                     required=True, empty_label="(Nothing)")

    total_number_of_locations = forms.IntegerField(required=True)

    def clean(self):

        cleaned_data = super(Organization_1_3, self).clean()

        is_use_ssn_for_user = cleaned_data.get("is_use_ssn_for_user")

        is_electronic_postings_enabled = cleaned_data.get("is_use_ssn_for_user")

        total_number_of_locations = cleaned_data.get("total_number_of_locations")

        organization = self.organization

        employee_sanction_monitoring = organization.billing.plan.modules.filter(short_code='ssn_for_each_user',
                                                                                 is_active=True).exists()

        if employee_sanction_monitoring is True:

            if is_use_ssn_for_user is None:
                raise forms.ValidationError('This field is required.')
            else:
                return cleaned_data

        if total_number_of_locations < organization.total_number_of_locations:
            msg = "You can\'t decrease total("+str(organization.total_number_of_locations)+") number of locations. However you can delete locations after completing initial step."
            self._errors["total_number_of_locations"] = self.error_class([msg])
        else:
            return cleaned_data

class Organization_1_4(forms.Form):
    """
    For admin_setup_organization_1_4
    """

    def __init__(self, *args, **kwargs):
        super(Organization_1_4, self).__init__(*args, **kwargs)
        services_offered = CoreServicesOffered.objects.filter(is_active=True)
        for service in services_offered:
            self.fields['%s' % service.short_code] = forms.BooleanField(required=False, label=service.name)


    services_consistent_all_locations = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(),
                                                               to_field_name='value', empty_label="(Nothing)")


class Organization_1_5(forms.Form):
    """
    For admin_setup_organization_1_4
    """
    modules_consistent = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value',
                                                empty_label="(Nothing)")


class Organization_1_6(forms.Form):
    """
    For admin_setup_organization_1_6
    """
    question = forms.CharField(widget=forms.HiddenInput(), label='')

    default_job_title = forms.CharField(max_length=100, required=False,

                                        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'', 'tabindex':'-1'}),
                                        label='Default Job Title*')

    organization_job_title = forms.CharField(max_length=100, required=True,
                                             validators=[custom_validator_valid_characters_space_with_and_sign],
                                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Organization Job Title'}),
                                             label='Organization Job Title*')

    first_name = forms.CharField(max_length=100, required=True, validators=[custom_validator_valid_characters_space],
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}), label='First Name*')

    last_name = forms.CharField(max_length=100, required=True, validators=[custom_validator_valid_characters_space],
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}), label='Last Name*')

    actual_job_title = forms.CharField(max_length=100, required=True,
                                       validators=[custom_validator_valid_characters_space_with_and_sign],
                                       widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Contact\'s Actual Job Title'}),
                                       label='Contact\'s Actual Job Title*')

    email = forms.EmailField(max_length=100, required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email Address'}), label='Email Address*')

    phone = forms.CharField(max_length=100, required=True, validators=[custom_validator_valid_phone_or_fax],
                            widget=forms.TextInput(attrs={'class': 'form-control phone_number', 'placeholder':'(xxx) xxx-xxxx'}), label='Direct Phone Number*')

    short_code = forms.CharField(widget=forms.HiddenInput(), label='')

    YES_OR_NO = (
        (0, 'No'),
        (1, 'Yes'),
    )

    is_organization_wide = forms.ChoiceField(required=True, choices=YES_OR_NO,
                                                label='Applies to Entire Company*', widget=forms.Select(attrs={'class': 'select-block select-yes-no', 'id':'selectpicker', 'type':'button'}))
    #is_organization_wide = forms.ModelChoiceField(queryset=UtilYesorNo.objects.all(), to_field_name='value', required=True, empty_label="(Nothing)")


