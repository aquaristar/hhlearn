from django.shortcuts import render
import datetime
from apps.utility.models import *
from apps.dashboard.models import *
import urllib, urllib2
#import simplejson
import json

def accreditation(request):
    #now = datetime.datetime.now()    
    profile = request.user.core_user_profile        

    #get accreditation agency data
    accreditation_data = {}
    if profile.department_id is not None:                
        container = profile.department               
    else:                
        container = profile.location
    
    if container.is_accredited_id == 1:        
        accreditation_agency = container.accreditation_agency
        
        #get address
        address = accreditation_agency.address1
        if accreditation_agency.address2 is not None:
            address = address + ' ' + accreditation_agency.address2
        
        accreditation_data = {'name': accreditation_agency.name,
                             'address': address,
                             'city': accreditation_agency.city,
                             'state': accreditation_agency.state,
                             'zip': accreditation_agency.zip,
                             'phone': accreditation_agency.phone,
                             'website': accreditation_agency.website,
                             'email': accreditation_agency.email,                             
                             }
        #get geocode from google maps
        gmap_url = "http://maps.googleapis.com/maps/api/geocode/json?"
        
        if accreditation_agency.city is not None:
            params = {'address': address+','+accreditation_agency.city}
        else:
            params = {'address': address}
        
        try:                
            gmap_address = urllib2.urlopen(gmap_url+urllib.urlencode(params))
            f = gmap_address.read()
            data = json.loads(f)
            if len(data['results']):
                accreditation_data['map_position'] = data['results'][0]['geometry']['location']           
        except Exception as e:
            gmap_address = None
        
        
        #get social media sites info for accreditation agency
        social_medias = AccreditingAgencySocialMedia.objects.filter(accreditingagency_id=accreditation_agency.id)
        smedias = []
        if len(social_medias) > 0:
            for obj in social_medias:
                sm_data = {'name': obj.socialmedia.social_media_name,
                           'short_code': obj.socialmedia.short_code,
                           'websites': obj.social_media_url,
                           'icon': obj.socialmedia.fa_icon,
                           'load_color': obj.socialmedia.load_color,
                           'hover_color': obj.socialmedia.hover_color,
                           }
                smedias.append(sm_data)
        accreditation_data['social_medias'] = smedias        
    
    return render(request, 'dashboard/accreditation/index.html', {'request': request, 'accreditation': accreditation_data})