from django.conf import settings
from django.shortcuts import render
from apps.admin.users.forms import *
from datetime import datetime
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from django.forms.models import model_to_dict

from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from apps.api.v1.utils.messages import *
from apps.utility.helpers import *

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import glob
import os
import shutil

def home(request):
    return render(request, 'admin/users/home.html', {'request': request})

def add(request):
    now = datetime.now()
    return render(request, 'admin/users/add.html', {'request': request})

def add_initial(request):
    
    #get user states
    organization = request.user.core_user_profile.core_organization.get(
                user_profiles__id=request.user.core_user_profile.id)
    users = organization.user_profiles.all().values_list('user_id', flat=True)
    status = UserStatus.objects.filter(user_id__in=users)
    if len(status) > 0:
        return HttpResponseRedirect(reverse('admin_users'))
    
    #get sample avatars images
    os.chdir(settings.STATIC_ROOT + "dashboard/common/images/avatars")
    sample_files = []
    for file in sorted(glob.glob("*.png")):
        #image_url = settings.STATIC_URL + "dashboard/common/images/avatars/" + file
        image_url = file
        sample_files.append(image_url)
    
    organization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)    
    #get user modules
    #modules = CoreUserProfilesModulesrequest.user.core_user_profile.modules.values()
    modules = CoreModules.objects.filter(is_active=1).order_by('name').values('id', 'name')     
    for module in modules:
        module_data = CoreModules.objects.get(id=module['id'])
        if module_data.core_user_profile_module is not None:
            if len(module_data.core_user_profile_module.filter(coreuserprofiles=request.user.core_user_profile,active_inactive=1)) == 1:
                module['active_inactive'] = 1
            else:
                module['active_inactive'] = 0
        else:
            module['active_inactive'] = 0
            
    #modules = CoreUserProfilesModules.objects.filter().values('id', 'active_inactive', 'coremodules__name')
        
    #get user locations       
    UserModulesFormset = formset_factory(UserModulesForm, can_delete=False, can_order=False, max_num=len(modules))
    
    if request.method == 'POST':
        request.user.email = decrypt_str(request.user.email)         
        form = UserInitialForm(request.POST, user=request.user)
        formset = UserModulesFormset(request.POST)                
        if form.is_valid():            
            #saving profile data
            cleaned_data = form.cleaned_data
            user = request.user
            #user.email = cleaned_data['email']
            #user.first_name = cleaned_data['first_name']
            #user.last_name = cleaned_data['last_name']
            user.email = encrypt_str(user.email)
            user.core_user_profile.job_title_id = cleaned_data['job_title']
            user.core_user_profile.location_id = cleaned_data['location']
            user.core_user_profile.phone_work = cleaned_data['phone_work']
            user.core_user_profile.phone_alternate = cleaned_data['phone_alternate']
            user.core_user_profile.phone_oncall = cleaned_data['phone_oncall']
            #user.set_password(cleaned_data['user_password'])
            
            if 'photo_file' in request.FILES and request.FILES['photo_file'] is not None:
                handle_uploaded_file(request.FILES['photo_file'], request.user)
            elif request.POST['sample_avatar'] is not None and request.POST['sample_avatar'] != "":
                upload_sample_image(request.POST['sample_avatar'], request.user)
            else:
                upload_sample_image('M-01.png', request.user)
            
            if 'employee_id' in form.fields: 
                user.core_user_profile.organization_id_number = cleaned_data['employee_id']
            if 'social_security_number' in form.fields:
                user.core_user_profile.user_social_security_number = cleaned_data['social_security_number']
            
            user.save()
            user.core_user_profile.save()
            
            #saving profile modules
            formset.is_valid()            
            for f in formset:                
                #module = CoreUserProfilesModules.objects.get(coreuserprofiles__id=request.user.core_user_profile.id, id=f.cleaned_data['id'])
                profile_modules = CoreUserProfilesModules.objects.filter(coreuserprofiles__id=request.user.core_user_profile.id, coremodules_id=f.cleaned_data['id'])
                if len(profile_modules) > 0:
                    module = profile_modules[0]
                    if 'active_inactive' in f.cleaned_data:
                        module.active_inactive = f.cleaned_data['active_inactive']
                    else:
                        module.active_inactive = False
                module.save()
            
            #activating user
            status = UserStatus.objects.create(user=user,
                                               status_date=datetime.now(),
                                               status=True,
                                               making_change_user=user)            
            status.save()
            #set user as administrator
            user_group = User.groups.through.objects.filter(user=user)
            if len(user_group) > 0:
                user_group = user_group[0] 
                g = Group.objects.get(id=2)
                user_group.group = g
                user_group.save()
            else:
                g = Group.objects.get(id=2) 
                g.user_set.add(user)
            #insert initial messages
            add_user_initial_message(request, user)                 
            return HttpResponseRedirect(reverse('admin_users'))
        else:
            formset = UserModulesFormset(initial=modules)
    else:
        request.user.email = decrypt_str(request.user.email)
        form = UserInitialForm(initial=model_to_dict(request.user), user=request.user)
        formset = UserModulesFormset(initial=modules)
        
    return render(request, 'admin/users/add_initial.html', {'form': form, 'formset': formset, 'request': request, 'sample_files': sample_files})

def handle_uploaded_file(f, user):
    ar = f.name.split('.')
    ext = ar[len(ar)-1]
    filename = settings.STATIC_ROOT + 'profile/images/'+str(user.id)+'.'+ext
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    url = settings.STATIC_URL + 'profile/images/'+str(user.id)+'.'+ext
    user.core_user_profile.photo_file = url    
    
    return

def upload_sample_image(file_name, user):
    #copy file name
    '''
    ar = file_name.split('.')
    ext = ar[len(ar)-1]
    src = settings.STATIC_ROOT + "dashboard/common/images/avatars/" + file_name
    dst = settings.STATIC_ROOT + "profile/images/" + str(user.id)+'.' + ext
    
    shutil.copyfile(src, dst)
    
    #save profile
     
    url = settings.STATIC_URL + 'profile/images/'+str(user.id)+'.'+ext
    '''
    url = settings.STATIC_URL + "dashboard/common/images/avatars/" + file_name
    user.core_user_profile.photo_file = url
    
    return

def edit(request, user_id=None): 
    return render(request, 'admin/users/edit.html', {'request': request})
    
    
    
    
    
    