"""
INFO
"""

# Importing render module from django
from django.shortcuts import render

from django.core.urlresolvers import reverse


# Importing redirect module from django.
from django.http import HttpResponseRedirect


# Importing LoginRegisterForm from website.core app

from forms import *


from django.contrib.auth.models import User
from django.contrib.auth.models import Group


def register(request):
    """
    INFO
    """

    # Check if it's a POST / user have submitted the form
    if request.method == 'POST':

        # We will use our own error display format which is described in "DivErrorList" in form
        form = RegisterForm(request.POST)

        # Now check if form is valid or not? validation rules can be modified in form.py
        if form.is_valid():

            # Well if form is valid then lets go create a user. I need to clean this code a bit :)
            user = User.objects.create_user(form.data['user_name'], form.data['email_address'], form.data['register_password'])

            # Lets select a group from database which user selected
            selected_group = Group.objects.get(name=form.data['membership_type'])

            # Now we have group information now lets add that group to user using ID
            user.groups.add(selected_group.id)

            # We need to set user INACTIVE on registration because we want them to confirm email first
            # So lets set is_active = 0
            user.is_active = 0

            # Now all we need to do is to save user model
            user.save()

            send_register_email(user.email)

            # Lets redirect user to thank you page
            return HttpResponseRedirect(reverse('register_successful'))

    # If it's not a POST request / user have not submitted form then just get default form values
    else:
        form = RegisterForm()

    # At the end we need to render the page and pass our form :)
    return render(request, 'register.html', {
        'form': form,
    })


def register_successful(request):
    """
    INFO
    """
    data = ''
    return render(request, 'register_successful.html', {
        'data': data,
    })

