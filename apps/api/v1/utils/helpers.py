import hashlib
from django.contrib.auth.models import User
import random
import os
import string
from rest_framework.authtoken.models import Token
import urllib
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

def validate_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError

    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def username_present(username):
    if User.objects.filter(username=username).count():
        return True

    return False


def email_present(email):
    if User.objects.filter(email=email).count():
        return True

    return False


def generate_random_string(length, stringset=string.ascii_letters + string.digits):
    '''
    Returns a string with `length` characters chosen from `stringset`
    >>> len(generate_random_string(20) == 20
    '''
    return ''.join([stringset[i % len(stringset)] \
                    for i in [ord(x) for x in os.urandom(length)]])


def generate_username():
    username = str(random.randint(0, 1000000000000))

    try:
        User.objects.get(username=username)
        return generate_username()
    except User.DoesNotExist:
        return username


def get_md5_hash(string=None):
    md5 = hashlib.md5()

    md5.update(string)

    return md5.hexdigest()


def username_present(username):
    if User.objects.filter(username=username).count():
        return True

    return False


def get_user(username):
    if User.objects.filter(username=username).count():
        return User.objects.get(username=username)

    return False


def email_present(email):
    if User.objects.filter(email=email).count():
        return True

    return False


def get_random_password():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pw_length = 14
    mypw = ""

    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]

    return mypw


def add_user(username, email, password, first_name, last_name):
    user = User.objects.create_user(username, email, password)

    user.first_name = first_name

    user.last_name = last_name

    user.save()

    if username_present(username):
        return True
    else:
        return False


    # helper function


def get_token(self, user, refresh=False):
    if refresh is False:

        try:
            token = Token.objects.get(user=user)

        except Token.DoesNotExist:

            token = Token.objects.create(user=user)

    elif refresh is True:

        try:
            token = Token.objects.get(user=user)

            token.delete()

            token = Token.objects.create(user=user)

        except Token.DoesNotExist:

            token = Token.objects.create(user=user)

    return token.key

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

register = template.Library()

@register.filter
@stringfilter
def qrcode(value, alt=None):
    """
    Generate QR Code image from a string with the Google charts API
    
    http://code.google.com/intl/fr-FR/apis/chart/types.html#qrcodes
    
    Exemple usage --
    {{ my_string|qrcode:"my alt" }}
    
    <img src="http://chart.apis.google.com/chart?chs=150x150&amp;cht=qr&amp;chl=my_string&amp;choe=UTF-8" alt="my alt" />
    """
    
    url = "http://chart.apis.google.com/chart?" + urllib.urlencode({'chs':'150x150', 'cht':'qr', 'chl':value, 'choe':'UTF-8'})
    alt = conditional_escape(alt or value)
    
    #return mark_safe(u"""<img class="qrcode" src="%s" width="150" height="150" alt="%s" />""" % (url, alt))
    return url

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False