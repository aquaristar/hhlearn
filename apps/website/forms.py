'''
INFO
'''

'''
importing normal forms
'''
from django import forms


'''
importing model forms
'''
from django.forms import ModelForm


class LoginForm(forms.Form):
    email_address = forms.EmailField()


class RegisterForm(forms.Form):
    email_address = forms.EmailField()


