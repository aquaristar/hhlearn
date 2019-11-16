from django.shortcuts import render
from apps.dashboard.models import *
from apps.resources.models import *
from datetime import datetime

def index(request):
    
    #get contact count    
    contact_count = 32
    #get faqs count
    faqs_count = 12    
    #get live chat count
    livechat_count = 100    
    #get community count
    community_count = 2    
    #get tutorials count
    tutorials_count = 1    
    #get industry links count
    industry_links_count = 44    
    #get industry events count
    industry_events_count = 670    
    #get accreditation count
    accreditation_count = 425    
    #get tools count
    tools_count = 25    
    #get newsletter count
    newsletter_count = 25
    #get social media count
    social_media_count = 25
    #get search site
    search_site = 'Aug 12'
    cur_date = datetime.now()
    
    #get accreditation count
    profile = request.user.core_user_profile        
    
    if profile.department_id is not None:                
        container = profile.department               
    else:                
        container = profile.location
    
    if container.is_accredited_id == 1:
        accreditation_agency = container.accreditation_agency
        if accreditation_agency is not None:
            accreditation = accreditation_agency.acronym
        else:
            accreditation = 'TBD'
    else:
        accreditation = 'TBD'
    
    count_data = {'contact': contact_count,
                  'faqs': faqs_count,
                  'livechat': livechat_count,
                  'community': community_count,
                  'tutorials': tutorials_count,
                  'industry_links': industry_links_count,
                  'industry_events': industry_events_count,
                  'accreditation': accreditation,
                  'tools': tools_count,
                  'newsletter': newsletter_count,
                  'social_media': social_media_count,
                  'search_site': search_site,
                  'cur_date': cur_date,
                 }
    
    return render(request, 'support/index.html', {'request': request, 'countData': count_data})


