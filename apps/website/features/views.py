from django.shortcuts import render
import datetime
from django.db.models import Q

from apps.dashboard.models import *
from apps.utility.models import *



#def features(request):
#    now = datetime.datetime.now()
#    return render(request, 'website/features/index.html', {'request': request})

def features_benefits(request):
    all_modules = CoreModules.objects.filter(is_active=True).order_by('name')
    sbe_modules = CoreModules.objects.filter(is_active=True, is_addon=False).order_by('name')
    pro_pricing = CoreUserPacks.objects.filter(id__gte=2, id__lte=12).order_by('monthly_price')[:7]
    sbe_pricing = CoreUserPacks.objects.filter(id__gte=22, id__lte=32).order_by('monthly_price')[:7]
    return render(  request, 
                    'website/features/benefits.html', 
                      {'request': request,
                       'all_modules': all_modules,
                       'sbe_modules': sbe_modules,
                       'pro_pricing': pro_pricing,
                       'sbe_pricing': sbe_pricing
                       })

def features_courses(request):
    categories = len(UtilResourceCategories.objects.filter(is_active=True))
    resource_sizes = len(UtilResourceSizes.objects.all())
    formats = len(UtilResourceFormats.objects.filter(is_active=True))
    forms = len(CoreResources.objects.filter(is_form=True, is_active=True))
    publications = len(CoreResources.objects.filter(is_publication=True, is_active=True))
    videos = len(CoreResources.objects.filter(is_video=True, is_active=True))
    report_categories = UtilReportCategories.objects.filter(is_active=True)
    return render(request, 
                  'website/features/courses.html', 
                  {'request': request,
                   'categories': categories,
                   'resource_sizes': resource_sizes,
                   'formats': formats,
                   'videos': videos,
                   'forms': forms,
                   'publications': publications,
                   'report_categories': report_categories,
                   })

def features_responsive(request):
    events = UtilIndustryEvents.objects.filter(is_active=True, will_hhlearn_be_there=True, remove_date_plus_one_day__gte=datetime.now()).order_by('event_start_date')[:3]    
    lms_systems = UtilLMSSystems.objects.filter(is_active=True).order_by('LMS_name')
    return render(request, 
                  'website/features/responsive.html', 
                  {'request': request, 
                   'lms_systems':lms_systems,
                   'events': events})

def features_terms(request):
    return render(request, 'website/features/terms.html', {'request': request})