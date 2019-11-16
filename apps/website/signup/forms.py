"""
All forms related to registrations are here.
"""

from validators import *

# Importing normal forms
from django import forms



from apps.utility.models import *

from apps.dashboard.models import *


# Importing User model from django auth because we are using django builtin authentication syste.
from django.contrib.auth.models import User


#
class SignUpForm(forms.Form):
    """
    RegisterForm handles all the main registration process and performs all the validations etc.
    """    
    # We need to provide list of memberships available for ChoiceField
    STATE_CHOICES = (
        ('Vendor', 'Vendor'),
        ('Home Owner', 'Home Owner'),
    )
    #membership_type = forms.ChoiceField(choices=STATE_CHOICES)
    #state = forms.ModelChoiceField(queryset=UtilUSAStates.objects.all(), required=True, empty_label="(Nothing)")
    state = forms.CharField(max_length=100, validators=[custom_validator_valid_characters_space])
    #user_name = forms.CharField(max_length=32, min_length=3, validators=[custom_validator_valid_characters, custom_validator_unique_user_name])
    email_address = forms.EmailField(validators=[custom_validator_unique_email])    
    confirm_email_address = forms.EmailField(validators=[custom_validator_unique_email])
    first_name = forms.CharField(max_length=100, validators=[custom_validator_valid_characters])
    last_name = forms.CharField(max_length=100, validators=[custom_validator_valid_characters])
    #password = forms.CharField(max_length=1024, validators=[custom_validator_password_requirement])
    #confirm_password = forms.CharField(max_length=1024, validators=[custom_validator_password_requirement])
    org_name = forms.CharField(max_length=100, validators=[custom_validator_valid_organization])
    street_address_1 = forms.CharField(max_length=100, validators=[custom_validator_valid_characters_space])
    street_address_2 = forms.CharField(max_length=100, required=False, validators=[custom_validator_valid_characters_space])
    city = forms.CharField(max_length=100, validators=[custom_validator_valid_characters_space])
    zip_code = forms.CharField(max_length=6, validators=[custom_validator_valid_zip])
    lead_source = forms.ModelChoiceField(queryset=UtilLeadSources.objects.filter(is_active=True).order_by('lead_source_name'), required=True)
    work_phone = forms.CharField(max_length=20, validators=[custom_validator_valid_phone_or_fax])    
    
    def clean(self):
        """
        This clean() method is executed automatically to check fields and I'm using it here to compare
        passwords.
        """
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        email = cleaned_data.get("email_address")
        confirm_email = cleaned_data.get("confirm_email_address")

        if password != confirm_password:
            # We know these are not in self._errors now (see discussion
            # below).
            msg = u"Passwords must be identical."
            self._errors["password"] = self.error_class([msg])
            self._errors["confirm_password"] = self.error_class([msg])

            # These fields are no longer valid. Remove them from the
            # cleaned data.
            #del cleaned_data["password"]
            #del cleaned_data["confirm_password"]
        if email != confirm_email:
            msg = u"Email must be identical."
            self._errors["email_address"] = self.error_class([msg])
            self._errors["confirm_email_address"] = self.error_class([msg])
            
        # Always return the full collection of cleaned data.
        return cleaned_data


class SignUpFormTerms(forms.Form):

    """
    RegisterForm handles all the main registration process and performs all the validations etc.
    """

    # we will check for error in Clean method because we need to add custom message.
    accept_terms = forms.BooleanField(required=False)

    email_terms = forms.BooleanField(required=False)

    def clean(self):
        """
        This clean() method is executed automatically to check fields and I'm using it here to compare
        passwords.
        """
        cleaned_data = super(SignUpFormTerms, self).clean()
        accept_terms = cleaned_data.get("accept_terms")

        if accept_terms is False:
            # We know these are not in self._errors now (see discussion
            # below).
            msg = u"Please accept terms of services."
            self._errors["accept_terms"] = self.error_class([msg])

            # These fields are no longer valid. Remove them from the
            # cleaned data.
            del cleaned_data["accept_terms"]

        # Always return the full collection of cleaned data.
        return cleaned_data


class SignUpPaymentForm(forms.Form):

    """
    RegisterForm handles all the main registration process and performs all the validations etc.
    """

    #membership_type = forms.ChoiceField(choices=STATE_CHOICES)

    membership_plan = forms.ModelChoiceField(queryset=CorePlans.objects.all(), required=True, empty_label="(Nothing)")

    user_pack = forms.ModelChoiceField(queryset=CoreUserPacks.objects.all(), required=True, empty_label="(Nothing)")

    payment_method = forms.ModelChoiceField(queryset=UtilPaymentMethods.objects.all(), required=True, empty_label="(Nothing)")

    credit_card_person_name = forms.CharField(max_length=100, required=False)

    credit_card_number = forms.IntegerField(required=False)

    card_expiry_month = forms.ModelChoiceField(queryset=UtilMonths.objects.all(),  empty_label="(Nothing)", required=False)

    card_expiry_year = forms.ModelChoiceField(queryset=UtilYears.objects.order_by('-year'), empty_label="(Nothing)", required=False)

    billing_address_1 = forms.CharField(max_length=100, validators=[custom_validator_valid_characters_space])

    billing_address_2 = forms.CharField(max_length=100, required=False, validators=[custom_validator_valid_characters_space])

    city = forms.CharField(max_length=100, validators=[custom_validator_valid_characters])

    state = forms.ModelChoiceField(queryset=UtilUSAStates.objects.all(), required=True, empty_label="(Nothing)")

    zip_code = forms.CharField(max_length=6, validators=[custom_validator_valid_zip])

    def clean(self):
        cleaned_data = super(SignUpPaymentForm, self).clean()

        payment_method = cleaned_data.get("payment_method")

        credit_card_person_name = cleaned_data.get("credit_card_person_name")

        credit_card_number = cleaned_data.get("credit_card_number")

        card_expiry_month = cleaned_data.get("card_expiry_month")

        card_expiry_year = cleaned_data.get("card_expiry_year")

        if payment_method is None:

            print 'not selected payment method yet'

        # 1 represents paypal
        elif payment_method.short_code == 'paypal':

            print 'using paypal'

        else:

            if credit_card_person_name is None:

                msg = u"This card_name is required."
                self._errors["credit_card_person_name"] = self.error_class([msg])

            if credit_card_number is None:

                msg = u"This field is required."
                self._errors["credit_card_number"] = self.error_class([msg])

            if card_expiry_month is None:

                msg = u"This field is required."
                self._errors["card_expiry_month"] = self.error_class([msg])

            if card_expiry_year is None:

                msg = u"This field is required."
                self._errors["card_expiry_year"] = self.error_class([msg])

        # Always return the full collection of cleaned data.
        return cleaned_data



