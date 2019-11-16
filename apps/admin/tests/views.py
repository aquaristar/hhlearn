from django.shortcuts import render
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from django.forms.models import model_to_dict

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from apps.admin.tests.forms import *

import datetime

def home(request):
    return render(request, 'admin/tests/home.html', {'request': request})

def add(request):
    now = datetime.datetime.now()
    '''
    if request.method == 'POST':
        form = TestForm(request.POST, user=request.user)
        if form.is_valid():
            pass
    else:
        form = TestForm(user=request.user)
    '''
    question_types = CoreQuestionTypes.objects.all()
    #accreditation_agencies = UtilRegAgencies.objects.all()
    #states = UtilUSAStates.objects.all()
    #county_fips = UtilZipCodes.objects.all()
     
    return render(request, 'admin/tests/add.html', {'request': request, 
                                                    #'form': form, 
                                                    'question_types': question_types,})
                                                    #'accreditation_agencies': accreditation_agencies,
     #                                               'states': states,
      #                                              'county_fips': county_fips})

def edit(request, test_id=None):
    now = datetime.datetime.now()
    return render(request, 'admin/tests/edit.html', {'request': request})
