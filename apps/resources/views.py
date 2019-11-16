from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.shortcuts import render
from django.db.models import Count

from apps.dashboard.models import *
from apps.resources.models import *

from apps.api.v1.utils.views import *
from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.helpers import *

import mimetypes
import os.path
from datetime import *

import base64
from shutil import *



def index(request):    
    #get forms count    
    forms_count = 32
    #get custom forms count
    custom_forms_count = 12    
    #get publications count
    publications_count = 100    
    #get custom publications count
    custom_publications_count = 2    
    #get videos count
    videos_count = 1    
    #get custom videos count
    custom_videos_count = 44
    #get glossary words count
    glossary_words_count = get_glossary_words_count(request)
    #get accreditation count
    accreditation_count = get_accreditation_count(request)
    #get images count
    images_count = get_images_count(request)
    #get data count
    data_count = 25
    
    count_data = {'forms': forms_count,
                  'custom_forms': custom_forms_count,
                  'publications': publications_count,
                  'custom_publications': custom_publications_count,
                  'videos': videos_count,
                  'custom_videos': custom_videos_count,
                  'images': images_count,
                  'accreditations': accreditation_count,
                  'glossary_words': glossary_words_count,
                  'data': data_count
                 }
    
    return render(request, 'resources/index.html', {'request': request, 'countData': count_data})

def files(request, code_encrypted=None):
    code = base64.urlsafe_b64decode(str(code_encrypted))
    code_array = code.split(",")
    
    if len(code_array) is not 2:
        response = HttpResponseNotFound()
        return response
    
    encrypted_id = code_array[0] 
    format = code_array[1]
    try:
        #copy files
        obj = CoreResources.objects.get(id=encrypted_id)
        src = settings.STATIC_ROOT + 'resources/files/' + format + '/' + str(obj.id) + '.' +format
        #dest = settings.STATIC_ROOT + 'resources/temp/' + obj.encrypted_resource_id + '.' + format            
        dest = settings.STATIC_ROOT + 'resources/temp/' + code_encrypted + '.' + format
        copyfile(src, dest)
        
        file_name = os.path.basename(dest)
        file_size = os.path.getsize(dest)
        mimetypes.init()
        mime_type_guess = mimetypes.guess_type(dest)
        
        fsock = open(dest,"r")
        if mime_type_guess is not None:
            response = HttpResponse(fsock, mimetype=mime_type_guess[0])
        
        if format == 'pdf' or format == 'png' or format == 'jpg':
            response['Content-Disposition'] = 'filename=' + file_name
        else:
            response['Content-Disposition'] = 'attachment;filename=' + file_name
        
        visited_obj = CoreResourcesVisited.objects.create(coreresources_id = obj.id,
                                                          user = request.user,
                                                          access_date_time_UTC = datetime.now(),
                                                          browser_used = request.META['HTTP_USER_AGENT'],
                                                          ip_address_of_user = get_client_ip(request)
                                                          )
        visited_obj.save()
        
        return response
    except IOError:
        response = HttpResponseNotFound()  

    return response
