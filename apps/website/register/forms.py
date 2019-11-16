"""
All forms related to registrations are here.
"""

from helpers import *

# Importing normal forms
from django import forms

# Importing User model from django auth because we are using django builtin authentication syste.
from django.contrib.auth.models import User


#
class RegisterForm(forms.Form):

    """
    RegisterForm handles all the main registration process and performs all the validations etc.
    """

    # We need to provide list of memberships available for ChoiceField
    MEMBERSHIP_CHOICES = (
        ('Vendor', 'Vendor'),
        ('Home Owner', 'Home Owner'),
    )

    membership_type = forms.ChoiceField(choices=MEMBERSHIP_CHOICES)

    user_name = forms.CharField(max_length=32, min_length=3, validators=[custom_validator_unique_user_check])

    first_name = forms.CharField(max_length=100)

    last_name = forms.CharField(max_length=100)

    """
        adding validator "unique_email_check" to check if email already exists in database or not?
    """
    email_address = forms.EmailField(validators=[custom_validator_unique_email_check])

    register_password = forms.CharField(max_length=100)



