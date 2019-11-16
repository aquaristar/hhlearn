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
from apps.api.v1.utils.mail import *
from django.conf import settings


class APIAuthReset(APIView, APIException):

	# POST will be used for login.
	def post(self, request):

		response = dict()

		# username
		username = self.request.DATA.get('username', None)

		# check if any field is missing.
		if not username:

			# missing field response
			response = response_missing_fields()

			# raising exception.
			raise ExceptionMissingFields(detail=response)

		if username_present(username) is False:

			# get predefined response for username already used
			response = response_username_do_not_exist()

			# raising exception
			raise ExceptionUsernameDoesNotExists(detail=response)

		# get the user we want to reset password for.
		user = User.objects.get(username=username)

		# don't let user reset password if account is not verified yet.
		if user.is_active == 0:

			# get response message
			response = response_account_no_activated()

			# raising exception
			raise ExceptionAccountNotActivated(detail=response)

		elif user.is_active == 1:

			# get user profile data
			user_profile = CoreUserProfiles.objects.get(user=user)

			# setting verification code.
			user_profile.password_reset_token = generate_random_string(25)

			user_profile.save()

			VERIFICATION_URL = settings.APP_URL + 'reset/' + user_profile.password_reset_token

			mail = SendEmail()

			mail.password_reset(recipient=user.email, VERIFICATION_URL=VERIFICATION_URL, FIRST_NAME=user.first_name, LAST_NAME=user.last_name)

			response = response_password_reset()

		# sending response and authentication token
		content = {
		'response': response,
		}

		# final response
		return Response(content, status=status.HTTP_200_OK)

	# PUT will be used for login.
	def put(self, request):

		response = dict()

		# username
		password = self.request.DATA.get('password', None)

		password_confirm = self.request.DATA.get('password_confirm', None)

		password_reset_token = self.request.DATA.get('password_reset_token', None)

		# if any of the fields is missing then show exception
		if not password or not password_confirm:

			# get predefined response for missing fields.
			response = response_missing_fields()

			# raise exception if any field is missing
			raise ExceptionMissingFields(detail=response)


		if password != password_confirm:

			# get response message
			response = response_passwords_not_same()

			# raising exception
			raise ExceptionPasswordNotMatch(detail=response)

		if CoreUserProfiles.objects.filter(password_reset_token__iexact=password_reset_token).exists():

			user_details = CoreUserProfiles.objects.get(password_reset_token__iexact=password_reset_token)

			user_details.user.set_password(password)

			# saving user password.
			user_details.user.save()

			user_details.password_reset_token = None

			user_details.save()

			response = response_password_updated()

		else:

			# get response message
			response = response_password_token_invalid()

			# raising exception
			raise ExceptionInvalidPasswordToken(detail=response)

		# sending response and authentication token
		content = {
		'response': response,
		}

		# final response
		return Response(content, status=status.HTTP_200_OK)