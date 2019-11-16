"""
All forms related to authentication are here.
"""

from apps.utility.validators import *

# Importing normal forms
from django import forms



from apps.utility.models import *


# Importing User model from django auth because we are using django builtin authentication syste.
from django.contrib.auth.models import User


#
class LoginForm(forms.Form):

    """
    RegisterForm handles all the main registration process and performs all the validations etc.
    """

    username = forms.CharField(max_length=32, required=True)

    password = forms.CharField(max_length=1024, required=True)

    remember_me = forms.BooleanField(required=False)
