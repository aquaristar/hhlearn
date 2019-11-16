import os
import string

# We should all know what this is used for by now.
from django.core.mail import send_mail

# get_template is what we need for loading up the template for parsing.
from django.template.loader import get_template

# Templates in Django need a "Context" to parse with, so we'll borrow this.
# "Context"'s are really nothing more than a generic dict wrapped up in a
# neat little function call.
from django.template import Context

from django.contrib.auth.models import User

from Crypto.Cipher import AES
from Crypto import Random
import base64
import hashlib


def generate_random_string(length, stringset=string.ascii_letters+string.digits):
    '''
    Returns a string with `length` characters chosen from `stringset`
    >>> len(generate_random_string(20) == 20
    '''
    return ''.join([stringset[i%len(stringset)] \
                    for i in [ord(x) for x in os.urandom(length)]])


def send_signup_email(user, profile):

    sender_email = 'email@bilal.me'

    # Our send_mail call revisited. This time, instead of passing
    # a string for the body, we load up a template with get_template()
    # and render it with a Context of the variables we want to make available
    # to that template.
    send_mail(
        'Thanks for signing up!',
        get_template('website/emails/signup.html').render(
            Context({
                'first_name': user.first_name,
                'last_name': user.last_name,
                'activation_token': profile.activation_token
            })
        ),
        sender_email,
        [user.email],
        fail_silently=False
    )


def send_terms_email(username):

    sender_email = 'email@bilal.me'

    user_details = User.objects.get(username__iexact=username)

    # Our send_mail call revisited. This time, instead of passing
    # a string for the body, we load up a template with get_template()
    # and render it with a Context of the variables we want to make available
    # to that template.
    send_mail(
        'Thanks for signing up!',
        get_template('website/emails/terms_of_services.html').render(
            Context({
                'first_name': user_details.first_name,
                'last_name': user_details.last_name,
            })
        ),
        sender_email,
        [user_details.email],
        fail_silently=False
    )


def send_templated_email(username, subject, email_template_name, email_context, recipients,
                         sender=None, bcc=None, fail_silently=False, files=None):

    """
    send_templated_mail() is a wrapper around Django's e-mail routines that
    allows us to easily send multipart (text/plain & text/html) e-mails using
    templates that are stored in the database. This lets the admin provide
    both a text and a HTML template for each message.

    email_template_name is the slug of the template to use for this message (see
        models.EmailTemplate)

    email_context is a dictionary to be used when rendering the template

    recipients can be either a string, eg 'a@b.com', or a list of strings.

    sender should contain a string, eg 'My Site <me@z.com>'. If you leave it
        blank, it'll use settings.DEFAULT_FROM_EMAIL as a fallback.

    bcc is an optional list of addresses that will receive this message as a
        blind carbon copy.

    fail_silently is passed to Django's mail routine. Set to 'True' to ignore
        any errors at send time.

    files can be a list of file paths to be attached, or it can be left blank.
        eg ('/tmp/file1.txt', '/tmp/image.png')

    """
    from django.conf import settings
    from django.core.mail import EmailMultiAlternatives
    from django.template import loader, Context
    from django.utils.html import strip_tags

    user_details = User.objects.defer("password").get(username__iexact=username)

    c = Context({
        'user_details': user_details,
    })

    if not sender:
        sender = settings.DEFAULT_FROM_EMAIL

    template = loader.get_template(email_template_name)

    text_part = strip_tags(template.render(c))
    html_part = template.render(c)

    if type(recipients) == str:
        if recipients.find(','):
            recipients = recipients.split(',')
    elif type(recipients) != list:
        recipients = [recipients,]

    msg = EmailMultiAlternatives(subject,
                                 text_part,
                                 sender,
                                 recipients,
                                 bcc=bcc)
    msg.attach_alternative(html_part, "text/html")

    if files:
        if type(files) != list:
            files = [files,]

        for file in files:
            msg.attach_file(file)

    return msg.send(fail_silently)

class AESCipher:

    def __init__(self, key): 
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
    
def encrypt_str(str):
    if str is None:
        return None
    if str == "":
        return ""
    secret_key = b'hhlearn security'
    cipher = AESCipher(secret_key) # never use ECB in strong systems obviously
    encoded = cipher.encrypt(str)
    return encoded
def decrypt_str(str):
    if str is None:
        return None
    if str == "":
        return ""
    secret_key = b'hhlearn security'
    cipher = AESCipher(secret_key)
    decoded = cipher.decrypt(str)
    return decoded