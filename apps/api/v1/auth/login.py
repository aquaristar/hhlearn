from django.views.generic import View
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.authentication import *
from apps.dashboard.models import *
from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.helpers import *


class APIAuthLogin(APIView, APIException):
    # POST will be used for login.
    def post(self, request):

        # check if any field is missing.
        if not self.request.DATA.get('username') or not self.request.DATA.get('password'):
            # missing field response
            response = response_missing_fields()

            # raising exception.
            raise ExceptionMissingFields(detail=response)

        # try to authenticate user. If username or password is empty then just use NONE.
        user = authenticate(username=self.request.DATA.get('username', None),
                            password=self.request.DATA.get('password', None))

        # check if user exists in database
        if user is not None:

            # check if user is active
            if user.is_active:

                # login user
                login(request, user)

                # generate new authentication for user.
                auth_token = get_token(self, user, refresh=True)

                # sending response after login is successful.
                response = response_login_successful()

            # if user account is not active.
            else:
                # get response for account not active condition
                response = response_account_not_active()

                # raise exception.
                raise ExceptionAccountNotActive(detail=response)

        # if user authentication fails
        else:

            response = response_authentication_failed()

            raise ExceptionAuthenticationFailed(detail=response)

        # sending response and authentication token
        content = {
        'response': response,
        'auth_token': auth_token,
        }

        # final response
        return Response(content, status=status.HTTP_200_OK)
