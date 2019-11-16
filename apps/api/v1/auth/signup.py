from rest_framework.views import APIView
from rest_framework.response import Response
from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.helpers import *
from apps.api.v1.utils.mail import *
from django.contrib.auth.models import User
from apps.dashboard.models import *
from django.conf import settings


class APIAuthSignup(APIView, APIException):

	response = dict()

	# signup will use post request.
	def post(self, request, format=None):

		# organization name
		org_name = self.request.DATA.get('org_name', None)

		# username
		username = self.request.DATA.get('username', None)

		# first name
		first_name = self.request.DATA.get('first_name', None)

		# last name
		last_name = self.request.DATA.get('last_name', None)

		# email address
		email = self.request.DATA.get('email', None)

		# password
		password = self.request.DATA.get('password', None)

		# if any of the fields is missing then show exception
		if not first_name or not last_name or not email or not password or not username or not org_name:

			# get predefined response for missing fields.
			response = response_missing_fields()

			# raise exception if any field is missing
			raise ExceptionMissingFields(detail=response)

		if validate_email(email) is False:

			# get predefined response for not valid email
			response = response_email_not_valid()

			# raising exception
			raise ExceptionEmailNotValid(detail=response)

		if username_present(username) is True:

			# get predefined response for username already used
			response = response_username_already_used()

			# raising exception
			raise ExceptionUsernameAlreadyExists(detail=response)

		if email_present(email) is True:

			# get predefined response for email already used
			response = response_email_already_used()

			# raising exception
			raise ExceptionEmailAlreadyExists(detail=response)

		# creating user
		user = User.objects.create_user(username, email, password)

		# assigning first name
		user.first_name = first_name

		# assigning first name
		user.last_name = last_name

		# We need to set user INACTIVE on registration because we want them to confirm email first
		# So lets set is_active = 0
		user.is_active = 0

		# save to database
		user.save()

		# if user was created successfully then we need to add organization as well.
		if user.id:

			# new object from organization model.
			organization = CoreOrganizations()

			# setting organization name
			organization.name = org_name

			# saving organization data.
			organization.save()

			# if organization is created successfully
			if organization.id:

				# we need to create a default group for primary user.
				group = CoreGroups()

				group.name = "Default"

				group.description = "Default group with all permissions. This group can't be deleted"

				group.is_default_group = True

				group.is_active = True

				group.email_required = False

				group.allow_password_reset = True

				group.allow_dashboard_login = True

				group.save()

				# adding user profile entry
				user_profile = CoreUserProfiles(user=user)

				# setting activation token for email verification and account activation.
				user_profile.email_verification_token = generate_random_string(25)

				# add user to group.
				selected_group = group

				# Need to link user group with user profile.
				user_profile.group = selected_group

				# Set first user as the org admin
				user_profile.is_org_admin = 1

				# saving data for user profile.
				user_profile.save()

				# adding user profile to organization.
				organization.user_profiles.add(user_profile)

				# adding group to organization.
				organization.groups.add(group)

				# get predefined response for email already used
				response = response_signup_successful()

				VERIFICATION_URL = settings.APP_URL + 'signup/verify/' + user_profile.email_verification_token

				mail = SendEmail()

				mail.signup_welcome(recipient=user.email, VERIFICATION_URL=VERIFICATION_URL, FIRST_NAME=user.first_name, LAST_NAME=user.last_name)

		# response content
		content = {
			'response': response,
		}

		# final response
		return Response(content, status=status.HTTP_200_OK)