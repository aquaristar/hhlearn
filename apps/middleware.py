from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse
from django.conf import settings


class SecureRequiredMiddleware(object):

    def __init__(self):
        self.paths = getattr(settings, 'SECURE_REQUIRED_PATHS')
        self.api_path = getattr(settings, 'API_PATH')
        self.https_enabled = self.paths and getattr(settings, 'HTTPS_ENABLED')

    def process_request(self, request):
        if self.https_enabled and not request.is_secure():
            for path in self.paths:
                if request.get_full_path().startswith(path):
                    request_url = request.build_absolute_uri(request.get_full_path())
                    secure_url = request_url.replace('http://', 'https://')
                    return HttpResponsePermanentRedirect(secure_url)

        if request.get_full_path().startswith(self.api_path):
            pass
        elif request.get_full_path().startswith('/certificate/'):
            pass
        elif request.get_full_path().startswith('/scoc/'):
            pass
        elif request.get_full_path().startswith('/scocd/'):
            pass
        # when user is resetting passsword.
        elif request.user.is_anonymous() and request.get_full_path().startswith(settings.PASSWORD_RESET_URL):
            pass        
        elif request.user.is_anonymous() and request.get_full_path().startswith(settings.SIGNUP_URL):
            pass        
        elif request.user.is_anonymous() and request.get_full_path() == settings.HOME_URL:
            pass
        elif request.user.is_anonymous() and request.get_full_path() in settings.FREE_URLS:
            pass        
        elif request.user.is_anonymous() and request.get_full_path() != settings.LOGIN_URL:
            return HttpResponsePermanentRedirect(settings.LOGIN_URL)
        elif request.user.is_authenticated() and request.get_full_path() == settings.LOGIN_URL:
            return HttpResponsePermanentRedirect(settings.DASHBOARD_URL)
        elif request.user.is_authenticated() and request.get_full_path() == settings.SIGNUP_URL:
            return HttpResponsePermanentRedirect(settings.DASHBOARD_URL)

class SignupMiddleware(object):

    def __init__(self):
        self.lock_signup_steps = getattr(settings, 'LOCK_SIGNUP_STEPS')

    def process_request(self, request):

        if request.user.is_anonymous() and request.get_full_path().startswith(settings.SIGNUP_URL):

            if 'signup_contact_info_complete' not in request.session:
                request.session['signup_contact_info_complete'] = False
                request.session['signup_terms_complete'] = False
                request.session['signup_payment_complete'] = False
                request.session['signup_contact_info_complete'] = False
                return HttpResponsePermanentRedirect(reverse('signup'))

            elif request.get_full_path().startswith('/signup/terms') and request.session['signup_contact_info_complete'] is False:
                return HttpResponsePermanentRedirect(reverse('signup'))

            elif request.get_full_path().startswith('/signup/payment') and request.session['signup_terms_complete'] is False:
                return HttpResponsePermanentRedirect(reverse('signup_terms'))

            elif request.get_full_path().startswith('/signup/thank_you') and request.session['signup_payment_complete'] is False:
                return HttpResponsePermanentRedirect(reverse('signup_payment'))

        elif request.get_full_path().startswith('/signup') and request.user.is_authenticated():
                return HttpResponsePermanentRedirect(reverse('dashboard'))

