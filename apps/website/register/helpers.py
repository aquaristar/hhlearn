# Importing normal forms
from django import forms

# Importing User model from django auth because we are using django builtin authentication syste.
from django.contrib.auth.models import User

from django.core.mail import send_mail


def custom_validator_unique_email_check(self):

        """
        Since we need to make sure that accounts are NOT created using same email
        so we need to make sure that email doesn't already exist in database.
        """

        data = self

        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already used")
        return data


def custom_validator_unique_user_check(self):

        """
        Since we need to make sure that accounts are NOT created using same email
        so we need to make sure that email doesn't already exist in database.
        """

        data = self

        if User.objects.filter(username=data).exists():
            raise forms.ValidationError("This username already used")
        return data


def send_register_email(email_address):

    send_mail('Subject here', 'Here is the message.', 'email@bilal.me',
              [email_address], fail_silently=False)