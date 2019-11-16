from rest_framework import serializers

from apps.dashboard.models import *
from apps.api.v1.utils.views import *
from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.helpers import *
from datetime import datetime
from datetime import timedelta

from apps.utility.helpers import *

from apps.api.v1.courses.serializers import *

from django.contrib.auth.models import Group
from django.contrib.auth.models import User

#serializers
class OrganizationMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreOrganizations
        fields = ('id', 'name')
class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreJobTitles
        fields = ('id', 'name')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreLocations
        fields = ('id', 'short_name')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreDepartments
        fields = ('id', 'short_name')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreRegions
        fields = ('id', 'short_name')

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreModules
        fields = ('id', 'name')

class ZipCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilZipCodes
        fields = ('id', 'zip_code', 'city_name', 'state_name')

#Serializers for User
class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField('get_user_type')
    email = serializers.SerializerMethodField('get_email')
    
    class Meta:
        model = User
        
    def get_user_type(self, obj):
        user_group = User.groups.through.objects.get(user=obj)
        return user_group.group_id
    
    def get_email(self, obj):
        return decrypt_str(obj.email)
        
class UserProfileModuleSerializer(serializers.ModelSerializer):
    coremodules = ModuleSerializer(many=False)
    class Meta:
        model = CoreUserProfilesModules        

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    modules = serializers.SerializerMethodField('get_profile_modules')
    organization_id_number = serializers.SerializerMethodField('get_organization_id_number')
    phone_work = serializers.SerializerMethodField('get_phone_work')
    phone_oncall = serializers.SerializerMethodField('get_phone_oncall')
    phone_alternate = serializers.SerializerMethodField('get_phone_alternate')
    home_address = serializers.SerializerMethodField('get_home_address')
    home_city = serializers.SerializerMethodField('get_home_city')
    home_zipcode = serializers.SerializerMethodField('get_home_zipcode')
    user_social_security_number = serializers.SerializerMethodField('get_user_social_security_number')
    
    class Meta:
        model = CoreUserProfiles
        fields = ('id', 'user', 'activation_token', 'requested_welcome_email', 'requested_tos_email', 'modules',
                    'location', 'department', 'region', 'job_title', 'gender', 'phone_work', 'organization_id_number',
                    'user_social_security_number', 'phone_oncall', 'phone_alternate', 'home_address',
                    'home_city', 'home_state', 'home_zipcode', 'photo_file', 'util_timezones',
                    'util_language_iso_codes', 'fontsize', 'subscribe_to_newsletter')
        
    #get all profile modules
    def get_profile_modules(self, obj):
        profile_modules = CoreUserProfilesModules.objects.filter(coreuserprofiles_id=obj.id)
        modules = UserProfileModuleSerializer(profile_modules).data
        return modules
    
    #get organization id number
    def get_organization_id_number(self, obj):
        return obj.organization_id_number
    
    #get phone work
    def get_phone_work(self, obj):
        return obj.phone_work
    
    #get phone oncall
    def get_phone_oncall(self, obj):
        return obj.phone_oncall
    
    #get phone alternate
    def get_phone_alternate(self, obj):
        return obj.phone_alternate
    
    #get home_address
    def get_home_address(self, obj):
        return obj.home_address
    
    #get home city
    def get_home_city(self, obj):
        return obj.home_city
    
    #get home zipcode
    def get_home_zipcode(self, obj):
        return obj.home_zipcode
    
    #get user_social_security_number
    def get_user_social_security_number(self, obj):
        return obj.user_social_security_number
    

class UserProfileMiniSerializer(serializers.ModelSerializer):
    job_title = serializers.SerializerMethodField('get_job_title')
    organization_id_number = serializers.SerializerMethodField('get_organization_id_number')
    phone_work = serializers.SerializerMethodField('get_phone_work')
    phone_oncall = serializers.SerializerMethodField('get_phone_oncall')
    phone_alternate = serializers.SerializerMethodField('get_phone_alternate')
    home_address = serializers.SerializerMethodField('get_home_address')
    home_city = serializers.SerializerMethodField('get_home_city')
    home_zipcode = serializers.SerializerMethodField('get_home_zipcode')
    user_social_security_number = serializers.SerializerMethodField('get_user_social_security_number')    
    
    class Meta:
        model = CoreUserProfiles
        fields = ('id', 'user', 'activation_token', 'requested_welcome_email', 'requested_tos_email', 'modules',
                    'location', 'department', 'region', 'job_title', 'gender', 'phone_work', 'organization_id_number',
                    'user_social_security_number', 'phone_oncall', 'phone_alternate', 'home_address',
                    'home_city', 'home_state', 'home_zipcode', 'photo_file', 'util_timezones',
                    'util_language_iso_codes', 'fontsize', 'subscribe_to_newsletter')
        
    def get_job_title(self, obj):
        if obj.job_title is not None:
            return obj.job_title.name
        return ""
    #get organization id number
    def get_organization_id_number(self, obj):
        return obj.organization_id_number
    
    #get phone work
    def get_phone_work(self, obj):
        return obj.phone_work
    
    #get phone oncall
    def get_phone_oncall(self, obj):
        return obj.phone_oncall
    
    #get phone alternate
    def get_phone_alternate(self, obj):
        return obj.phone_alternate
    
    #get home_address
    def get_home_address(self, obj):
        return obj.home_address
    
    #get home city
    def get_home_city(self, obj):
        return obj.home_city
    
    #get home zipcode
    def get_home_zipcode(self, obj):
        return obj.home_zipcode
    
    #get user_social_security_number
    def get_user_social_security_number(self, obj):
        return obj.user_social_security_number

class UserDetailSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profile')    
    class Meta:
        model = User
    def get_profile(self, obj):
        profile = CoreUserProfiles.objects.get(user_id=obj.id)
        return UserProfileMiniSerializer(profile).data
