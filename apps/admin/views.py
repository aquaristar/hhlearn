from django.shortcuts import render
from apps.api.v1.utils.views import *

import datetime


def home(request):
    #get glossary words count
    glossary_words_count = get_glossary_words_count(request)
    
    #get accreditation count
    accreditation_count = get_accreditation_count(request, True)
    
    #get images count
    images_count = get_images_count(request)
    
    count_data = {'images': images_count,                  
                  'glossary_words': glossary_words_count,
                  'accreditations': accreditation_count,                 
                 }
    return render(request, 'admin/index.html', {'request': request, 'countData': count_data})

