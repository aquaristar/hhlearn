from django.shortcuts import render
import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def home(request):
    now = datetime.datetime.now()
    return render(request, 'admin/setup/index.html', {'request': request})

def complete(request):
    user = request.user
    user_profile = request.user.core_user_profile
    orgaization = request.user.core_user_profile.core_organization.get(user_profiles__id=request.user.core_user_profile.id)
    organization.activation_date = datetime.now()
    organization.is_active_id = 1
    organization.save()
    
    return HttpResponseRedirect(reverse('admin_users_add_initial'))

