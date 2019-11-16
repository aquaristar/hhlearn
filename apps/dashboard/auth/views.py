# Importing render module from django
from django.shortcuts import render

# reverse is used to get the ful urls with just name.
from django.core.urlresolvers import reverse


# HttpResponseRedirect is used to redirect from one
# page to another.
from django.http import HttpResponseRedirect

#  authenticate is used to check for valid username and password
#  login used to actually login user. What we get from authentication
#  is actually sent to login.
from django.contrib.auth import authenticate, login

# this module have forms so we are just importing all the forms.
from forms import *

# this is django builtin method used to logout users and then redirect
# them to login page.
from django.contrib.auth.views import logout_then_login


def auth_login(request):
    """
    This auth_login method is used for login form. It basically checks for
    the username and password and also checks if user is activated or not?
    If not activated then it will show message to user accordingly.
    """

    # check if request is POST or not?
    # POST happens when user sumit the form.
    if request.method == 'POST':

        # now we to pass the whole post to our form which we created to check for validation etc.
        form = LoginForm(request.POST)

        # check if all the fields passes validation rules defined in forms file or not?
        if form.is_valid():

            # get the username from form data.
            username = form.data['username']

            # get password from form data.
            password = form.data['password']

            # since we have user name and password now we can try authentication.
            # if authentication passes then we will get respective user.
            user_details = authenticate(username=username, password=password)

            # check if we got the user details or not?
            # if NOT then it means validation failed.
            if user_details is not None:

                # now chekc if user is active or not?
                if user_details.is_active:

                    # On login form we have remember me checkbox.
                    # if user selected that checkbox then we need to
                    # extend the session expiry.
                    if form['remember_me'].data is True:

                        # "set_expiry(0)" means that session will be store for
                        # unlimited time unless user logout.
                        request.session.set_expiry(0)

                    # this is important, to actually LOGON USER IN we need to do following.
                    login(request, user_details)

                    # now everything went well, so we need to send message and message type
                    # to user interface.
                    request.session['message'] = "User is valid, active and authenticated"

                    request.session['message_code'] = "success"

                    # in urls.py file have have URL with dashboard URL.
                    # following line is just redirecting user to dashboard.
                    # NOTE :: move this to settings file.
                    return HttpResponseRedirect(reverse('dashboard'))

                # if user is not active then show following message on interface.
                else:

                    request.session['message'] = "The password is valid, but the account has been disabled!"

                    request.session['message_code'] = "error"

            # if username/password is not correct then show following message to interface.
            else:

                request.session['message'] = "The username and password were incorrect."

                request.session['message_code'] = "error"

        # this else gets executed if form is not valid. For security we will simply show that
        # username or password is invalid.
        else:

            request.session['message'] = "The username and password were incorrect."

            request.session['message_code'] = "error"

    # if request if not post then simply load the form.
    else:

        form = LoginForm()


    # We need to return form and request object.
    # request will hold all data related to user and
    # it will be used to check if user is logged in not?
    return render(request, 'dashboard/auth/login/index.html', {
        'form': form,
        'request': request,
    })


def auth_logout(request):
    """
    auth_logout method is fairly simple.
    All we do is use django built in function to logout and then
    redirect user to login page again.
    """
    #return logout_then_login(request, login_url=reverse('dashboard_login'))
    return logout_then_login(request, login_url='/')
