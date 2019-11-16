# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render
import reportlab
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.http import Http404
import time
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import letter, A4, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from rlextra.rml2pdf import rml2pdf

#import ho.pisa as pisa
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Template, Context
from cgi import escape

from datetime import datetime
from datetime import timedelta

from apps.api.v1.utils.views import *
from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.helpers import *

from apps.dashboard.models import *

import base64

import StringIO, cStringIO
import PIL
import urllib, urllib2

def course(request, course_code_encrypted=None):
    return render(request, 'dashboard/courses/index.html', {'request': request})

def print_pdf(request, course_code_encrypted=None):
    #get course
    course_id = base64.urlsafe_b64decode(str(course_code_encrypted))
    if test_attempt_id is not None:
        try:
            test_attempt = CoreTestAttempts.objects.get(id=test_attempt_id)
        except CoreTestAttempts.DoesNotExist:
            return render(request, 'pages/404.html', {'request': request})
    else:
        return render(request, 'pages/404.html', {'request': request})
    
    #get all course pages
    page = CoreCourses.objects.get(short_name=obj.short_name).pages.all.order_by(page_number)
    #convert replace tags in pages content    
    for page in pages:
        pages.append(replace_tags(request, page.raw_html))
        
    t = get_template('dashboard/course/rml_course_pages.html')
    c = Context({"course": course,})
    rml = t.render(c)
    
    #django templates are unicode, and so need to be encoded to utf-8        
    rml = rml.encode('utf8')
    rml = rml.replace("&", "&amp;")
    buf = cStringIO.StringIO()
    
    #create the pdf
    rml2pdf.go(rml, outputFileName=buf)
    buf.reset()
    pdfData = buf.read()
    
    #send the response
    response = HttpResponse(content_type='application/pdf')
    response.write(pdfData)
    response['Content-Disposition'] = 'filename="' + cert_code + '.pdf"'
    return response
    


