from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import serializers
from apps.api.v1.utils.exceptions import *

from apps.api.v1.utils.responses import *
from apps.dashboard.models import *
from apps.utility.models import *
from apps.utility.helpers import *

#language serializer
class UtilLanguagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UtilLanguageIsoCodes

#timezone serializer
class UtilTimezonesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UtilTimezones

#fontsize serializer
class UtilFontSizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilFontSizes
        
# user serializer.
class UserSerializer(serializers.ModelSerializer):
        
    photo_file = serializers.SerializerMethodField('get_user_photo')
    email = serializers.SerializerMethodField('get_email')
    
    class Meta:
        # model we want to use with serializer.
        model = User
        exclude = ('password',)
    
    def get_user_photo(self, obj):
        return obj.core_user_profile.photo_file
    
    def get_email(self, obj):
        return decrypt_str(obj.email)

# user serializer.
class StateSerializer(serializers.ModelSerializer):

    class Meta:
        # model we want to use with serializer.
        model = UtilUSAStates


# user serializer.
class LocationSerializer(serializers.ModelSerializer):

    state = StateSerializer()

    class Meta:
        # model we want to use with serializer.
        model = CoreLocations


# user serializer.
class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        # model we want to use with serializer.
        model = CoreDepartments


# user serializer.
class JobTitleSerializer(serializers.ModelSerializer):

    class Meta:
        # model we want to use with serializer.
        model = CoreJobTitles


# user profile serializer.
class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()    
    util_language_iso_codes = UtilLanguagesSerializer()    
    util_timezones = UtilTimezonesSerializer()
    fontsize = UtilFontSizesSerializer()
    location = LocationSerializer()
    #department = DepartmentSerializer()
    job_title = JobTitleSerializer()
    
    class Meta:
        # model we want to use with serializer.
        model = CoreUserProfiles


# organization serializer.
class OrganizationSerializer(serializers.ModelSerializer):
    user_profiles = UserProfileSerializer(many=True)

    class Meta:
        # model we want to use with serializer.
        model = CoreOrganizations


# Class based view for profile page.
class APIProfile(APIView):
    # this will be executed ONLY on GET request.
    def get(self, request, format=None):

        try:

            # need to get logged in user.
            user_profile = request.user.core_user_profile

            # sending logged in user data to serializer.
            user_profile_serializer = UserProfileSerializer(user_profile)

        except:

            # set data to None
            user_profile = None

            # sending blank data to serializer.
            user_profile_serializer = UserProfileSerializer(user_profile)

        # finalizing our output content.
        content = {
            # this node will have all organization related data
            'profile': user_profile_serializer.data,

        }

        # sending final response.
        return Response(content)

    # this will be executed ONLY on POST request.
    def post(self, request, format=None):

        email = self.request.DATA.get('email', None)

        first_name = self.request.DATA.get('first_name', None)

        last_name = self.request.DATA.get('last_name', None)

        address = self.request.DATA.get('address', None)

        city = self.request.DATA.get('city', None)

        state = self.request.DATA.get('state', None)

        postal_code = self.request.DATA.get('postal_code', None)

        country = self.request.DATA.get('country', None)

        phone = self.request.DATA.get('phone', None)

        try:

            user = request.user

            user.email = email

            user.first_name = first_name

            user.last_name = last_name

            user.save()

            # need to get logged in user.
            user_profile = request.user.core_user_profile_user

            user_profile.address = address

            user_profile.city = city

            user_profile.state = state

            user_profile.postal_code = postal_code

            user_profile.country = country

            user_profile.phone = phone

            user_profile.save()

            response = response_profile_save_successful()

            # if there's any exception then just send None data.
        except:

            response = response_profile_save_successful()

            raise ExceptionUnknownError(detail=response)

        # finalizing our output content.
        content = {  # sending success response
                     'response': response

        }

        # sending final response.
        return Response(content)


# Class based view for profile page.
class APIProfileMin(APIView):
    # this will be executed ONLY on GET request.
    def get(self, request, format=None):

        try:
            # sending user object to serializer to get JSON back
            user_serializer = UserSerializer(request.user)

        except:

            # setting user to None.
            user_serializer = UserSerializer(None)

        # finalizing our output content.
        content = {
            'profile': user_serializer.data,
        }

        # sending final response.
        return Response(content)
