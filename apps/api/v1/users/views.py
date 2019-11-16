from django.views.generic import Viewfrom rest_framework.views import APIViewfrom rest_framework.response import Responsefrom rest_framework import authentication, permissionsfrom rest_framework import serializersfrom rest_framework.parsers import *from apps.dashboard.models import *from apps.api.v1.utils.views import *from apps.api.v1.utils.exceptions import *from apps.api.v1.utils.responses import *from apps.api.v1.utils.helpers import *from apps.api.v1.utils.messages import *from apps.utility.helpers import *from datetime import datetimefrom datetime import timedeltafrom apps.api.v1.courses.serializers import *from apps.api.v1.users.serializers import *from django.contrib.auth.models import Groupfrom django.contrib.auth.models import Userfrom django.conf import settingsfrom django.core.mail import send_mailfrom django.core.mail import EmailMessageimport stringimport randomimport timeimport mathimport globimport osimport shutilimport base64import json#The API View class for the user add or edit actionclass APIUserAddEdit(APIView):    parser_classes = (FormParser, MultiPartParser, )    def get(self, request, format=None):                     user_id = self.request.QUERY_PARAMS.get('user_id', None)             #get test data                if user_id is None or user_id == "" or int(user_id) == -1:            profile_data = None            #get current user's organization            organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)            #get job titles for current user's organization            job_titles = organization.job_titles.order_by('name').all()            job_titles_data = JobTitleSerializer(job_titles).data              #get locations for current user's organization            locations = organization.locations.order_by('short_name').all()            locations_data = LocationSerializer(locations).data            #get modules            modules = CoreModules.objects.filter(is_active=1).order_by('name').values('id', 'name')            modules_data = ModuleSerializer(modules).data                    else:            try :                user_profile = CoreUserProfiles.objects.get(id=user_id)                profile_data = UserProfileSerializer(user_profile).data                              #get current user's organization                organization = user_profile.core_organization.get(user_profiles__id=user_profile.id)                #get job titles for current user's organization                job_titles = organization.job_titles.order_by('name').all()                job_titles_data = JobTitleSerializer(job_titles).data                #get locations for current user's organization                locations = organization.locations.order_by('short_name').all()                locations_data = LocationSerializer(locations).data                            except Exception as e:                 if hasattr(e, 'detail'):                    response = e.detail                else:                    response = dict()                    response['message'] = str(e.message)                    response['status'] = 'error'                raise ExceptionDefault(detail=response)                          #get sample avatars images        os.chdir(settings.STATIC_ROOT + "dashboard/common/images/avatars")        sample_files = []        for file in sorted(glob.glob("*.png")):            #image_url = settings.STATIC_URL + "dashboard/common/images/avatars/" + file            image_url = file            sample_files.append(image_url)                #get departments        departments = CoreDepartments.objects.filter(is_active=True)        departments_data = DepartmentSerializer(departments).data        #get regions        regions = CoreRegions.objects.filter()        regions_data = RegionSerializer(regions).data        #get user types        user_types = Group.objects.all()        user_types_data = UserTypeSerializer(user_types).data                content = {'status': 'success',                   'sample_photos': sample_files,                   'profile': profile_data,                   'job_titles': job_titles_data,                   'locations': locations_data,                   'departments': departments_data,                   'regions': regions_data,                   'user_types': user_types_data,                   }                if user_id == "" or user_id is None or int(user_id) == -1:             content['modules'] = modules_data              return Response(content)           def post(self, request, format=None):                profile = self.request.DATA.get('profile', None)        if profile is not None and profile is not "":            profile = json.loads(profile)                if profile is not None:            #add new user            if profile['id'] == -1:                user = User.objects.create_user(profile['user']['username'], encrypt_str(profile['user']['email']))                user.set_password(profile['user']['password'])                #user.save()                                user_profile = CoreUserProfiles.objects.create(user_id=user.id,                                                               location_id=profile['location'],                                                               job_title_id=profile['job_title'],                                                                                                                              region_id=profile['region'],                                                               user_social_security_number=profile['user_social_security_number'],                                                               phone_work=profile['phone_work'],                                                               phone_oncall=profile['phone_oncall'],                                                               phone_alternate=profile['phone_alternate'],                                                               organization_id_number=profile['organization_id_number'],                                                               home_state_id=1,                                                               util_timezones_id=5,                                                               util_language_iso_codes_id=1,                                                               fontsize_id=2,)                #user default settings                location = CoreLocations.objects.get(id=profile['location'])                #user_profile.util_timezones_id = location.timezone_id                                #add user type                g = Group.objects.get(id=profile['user']['type'])                 g.user_set.add(user)                                #add user messages and milestones for signup                add_user_signup_message(request, user)                add_user_signup_milestones(request, user)                                                        #change user data            else:                                               user_profile = CoreUserProfiles.objects.get(id=profile['id'])                user = user_profile.user                user_profile.location_id = profile['location']                user_profile.job_title_id = profile['job_title']                                                                               user_profile.region_id = profile['region']                user_profile.user_social_security_number = profile['user_social_security_number']                user_profile.phone_work = profile['phone_work']                user_profile.phone_oncall = profile['phone_oncall']                user_profile.phone_alternate = profile['phone_alternate']                user_profile.organization_id_number = profile['organization_id_number']                '''                user_profile.user_social_security_number = '123-45-6789'                user_profile.phone_work = '(209) 555-1212'                user_profile.phone_oncall = '(209) 555-1213'                user_profile.phone_alternate = '(209) 555-1213'                user_profile.organization_id_number = 'EMP-002'                user_profile.home_address = '123 Main Street'                user_profile.home_city = 'Fresno'                user_profile.home_zipcode = '93741'                '''                #change user name and email                user.username = profile['user']['username']                user.email = encrypt_str(profile['user']['email'])                #change user type                user_group = User.groups.through.objects.get(user=user)                g = Group.objects.get(id=profile['user']['type'])                user_group.group = g                user_group.save()                        if profile['department'] != "":                user_profile.department_id = int(profile['department'])                                                                        #insert profile module data            for module_data in profile['modules']:                module = None                if 'id' in module_data:                    module = CoreUserProfilesModules.objects.get(id=module_data['id'])                    module.active_inactive = module_data['active_inactive']                else:                    module = CoreUserProfilesModules.objects.create(coreuserprofiles_id=user_profile.id,                                                                    coremodules_id=module_data['coremodules']['id'],                                                                    active_inactive=module_data['active_inactive'],                                                                    date=datetime.now())                module.save()            user.first_name = profile['user']['first_name']            user.last_name = profile['user']['last_name']            user.is_active = profile['user']['is_active']                        user.set_password(profile['user']['password'])                                    #change users photo            photo_url = None                              if 'file' in request.FILES:                f = request.FILES['file']                ar = f.name.split('.')                ext = ar[len(ar)-1]                filename = settings.STATIC_ROOT + 'profile/images/'+str(user.id)+'.'+ext                with open(filename, 'wb+') as destination:                    for chunk in f.chunks():                        destination.write(chunk)                photo_url = settings.STATIC_URL + 'profile/images/'+str(user.id)+'.'+ext                        elif 'sample_avatar' in profile:                file_name = profile['sample_avatar']                if file_name != "" and file_name is not None:                    photo_url = settings.STATIC_URL + "dashboard/common/images/avatars/" + file_name                        if photo_url is not None:                user_profile.photo_file = photo_url            #save user and user profile's data            user.save()            # set organization            user_profile.save()            organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)            if len(CoreOrganizations.objects.filter(user_profiles__id=user_profile.id)) == 0:                organization.user_profiles.add(user_profile)                        #get users serialize data            profile_data = UserProfileSerializer(user_profile).data                    content = {'status': 'success',                    'profile': profile_data }        else:            content = {'status': 'fail',                       'message': 'Data is not correct'}        return Response(content)#The API Class to get users all listclass APIUsers(APIView):     def get(self, request, format=None):         user = request.user         users = User.objects.all()#.exclude(id=user.id)         users_data = UserDetailSerializer(users).data         content = { 'status': 'success',                     'users': users_data }         return Response(content)#The API class to activate userclass APIUser(APIView):    def get(self, request, format=None):        content = { 'status': 'success'}        return Response(content)    def post(self, request, format=None):        user_id = self.request.DATA.get('user_id', None)        method = self.request.DATA.get('method', None)        if user_id == None:            content = { 'stauts': 'fail',                        'message': 'User Id is undefined!'}            return Response(content)        try:            user = User.objects.get(id=user_id)            #activate user            if method == "activate":                                is_active = self.request.DATA.get('is_active', None)                                if is_active is not None:                    #save user activation data                                    user.is_active = is_active                    user.save()                    #record activation status                    status = UserStatus.objects.create(user_id = user.id,                                                       status_date = datetime.now(),                                                       status = is_active,                                                       making_change_user_id = request.user.id)                    status.save()                content = {'status': 'success',}                        except Exception as e:            content = { 'stauts': 'fail',                        'message': e.message}            return Response(content)                return Response(content)#get states and city info for zip codes       class APIUserZipCodes(APIView):    def get(self, request, format=None):        zip_code = self.request.QUERY_PARAMS.get('zipcode', None)        if zip_code is None:            content = { 'status': 'fail'}                    else:            zip_codes = UtilZipCodes.objects.filter(zip_code=zip_code)            data = ZipCodesSerializer(zip_codes).data            content = { 'status': 'success',                        'zip_codes': data }                return Response(content)