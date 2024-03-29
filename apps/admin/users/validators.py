# Importing normal forms
from django import forms

import re

# Importing User model from django auth because we are using django builtin authentication syste.
from django.contrib.auth.models import User
from apps.utility.models import *

from django.core.mail import send_mail


def custom_validator_unique_email(self):
    """
    Since we need to make sure that accounts are NOT created using same email
    so we need to make sure that email doesn't already exist in database.
    """

    data = self

    if User.objects.filter(email=data).exists():
        raise forms.ValidationError("This email already used")
    return data


def custom_validator_unique_user_name(self):
    """
    Since we need to make sure that accounts are NOT created using same email
    so we need to make sure that email doesn't already exist in database.
    """

    data = self

    if User.objects.filter(username=data).exists():
        raise forms.ValidationError("This username already used")
    return data


def custom_validator_valid_zip(self):
    """
    Since we need to make sure that accounts are NOT created using same email
    so we need to make sure that email doesn't already exist in database.
    """

    zip_code = self

    if UtilZipCodes.objects.filter(zip_code=zip_code).exists():
        return zip_code
    else:
        raise forms.ValidationError("Zip code is not valid.")


def custom_validator_valid_characters(self):
    """
    check if username is valid. we only allow letters, numbers, hyphens and underscores.
    """
    data = self

    if not re.match('^[\w-]+$', data):
        raise forms.ValidationError("This value must contain only letters, numbers, hyphens and underscores.")
    return data


def custom_validator_valid_phone_or_fax(self):
    """
    check if username is valid. we only allow letters, numbers, hyphens and underscores.
    """
    data = self

    if not re.match('^\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$', data):
        raise forms.ValidationError("Phone or Fax number should be formatted like (905)123-4567")
    return data


def custom_validator_valid_email(self):
    """
    check if username is valid. we only allow letters, numbers, hyphens and underscores.
    """
    data = self

    if not re.match('^([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})$', data):
        raise forms.ValidationError("Please provide valid email.")
    return data


def custom_validator_credit_card(self):
    """
    check if username is valid. we only allow letters, numbers, hyphens and underscores.
    """
    data = self

    if not re.match('^[0-9+]*$', data):
        raise forms.ValidationError("This value must contain only numbers.")
    return data


def custom_validator_password_requirement(self):
    """
    check if username is valid. we only allow letters, numbers, hyphens and underscores.
    """
    data = self

    if not re.match('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{5,32}$', data):
        raise forms.ValidationError(
            "Password must be at least 5 characters and must include at least one upper case letter, one lower case letter, and one numeric digit.")
    return data


def custom_validator_password_compare(self):
    """
    check if username is valid. we only allow letters, numbers, hyphens and underscores.
    """
    data = self

    if password != confirm_password:
        raise forms.ValidationError("Passwords must be identical.")
    return data


def custom_validator_valid_characters_space(self):
    """
    check if username is valid. we only allow letters, numbers, hyphens and underscores.
    """
    data = self

    #if not re.match('^[a-zA-Z0-9~@#$^*()_+=[\]{}|\\,.?: -]*$', data):
    #raise forms.ValidationError("This value must contain only letters, numbers, hyphens, underscores and spaces.")
    return data

def custom_validator_valid_organization(self):    
    data = self

    #if not re.match('^[a-zA-Z0-9~@#$^*()_+=[\]{}|\\,.?: -]*$\s\s+', data):
    #    raise forms.ValidationError("This value must contain only letters, numbers, hyphens, underscores and spaces.")
    return data


def custom_validator_valid_characters_space_with_and_sign(self):
    """
    check if username is valid. we only allow letters, numbers, hyphens and underscores.
    """
    data = self
    if not re.match('^[a-zA-Z0-9][A-Za-z0-9_-]|[&]*$', data):
        raise forms.ValidationError("This value must contain only letters, numbers, hyphens, underscores and spaces.")
    return data
