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

def fetch_resources(uri, rel):
    """
    Callback to allow pisa/reportlab to retrieve Images,Stylesheets, etc.
    `uri` is the href attribute from the html link element.
    `rel` gives a relative path, but it's not used here.

    """
    path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    return path

def certificate(request, cert_code_encrypted=None):
        
    #get test attempt object
    cert_code = base64.urlsafe_b64decode(str(cert_code_encrypted))
    
    test_attempt_id = None
    try:    
        test_attempt_id = decryptnumber(cert_code[:13])
    except:
        try:
            test_attempt_id = decryptnumber(cert_code[:12])
        except:
            try:
                test_attempt_id = decryptnumber(cert_code[:11])
            except:
                try:
                    test_attempt_id = decryptnumber(cert_code[:10])
                except:
                    try:
                        test_attempt_id = decryptnumber(cert_code[:9])
                    except:
                        return render(request, 'pages/404.html', {'request': request})
    
    if test_attempt_id is not None:
        try:
            test_attempt = CoreTestAttempts.objects.get(id=test_attempt_id)
        except CoreTestAttempts.DoesNotExist:
            return render(request, 'pages/404.html', {'request': request})
    else:
        return render(request, 'pages/404.html', {'request': request})
    
    pdfmetrics.registerFont(TTFont('BebasNeue', settings.STATIC_ROOT+'fonts/bebasneue-webfont.ttf'))
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="' + cert_code + '.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    p.drawImage(settings.STATIC_ROOT+'dashboard/certificate/images/bk_blue_general_knowledge_blank1.png', 0,0, width=738,height=558,mask=None)
    p.setPageSize((738, 558))  
    
    #Draw User Name
    user_name = test_attempt.user.first_name + ' ' + test_attempt.user.last_name
    str_len = len(user_name)
    str_width = p.stringWidth(user_name, 'BebasNeue', 70)
    p.setFont("BebasNeue", 70)
    x = 369-int(str_width/2)
    p.drawString(x, 310, user_name)
    
    #Draw Course Name
    course_name = test_attempt.test.course.name
    str_len = len(course_name)
    str_width = p.stringWidth(course_name, 'BebasNeue', 35)
    p.setFont("BebasNeue", 35)
    x = 369-int(str_width/2)
    p.drawString(x, 235, course_name)
    
    #Draw Test Passed Date
    #date = test_attempt.start_time + timedelta(seconds=test_attempt.seconds_taken)
    date = convert_timezone(test_attempt.grade_date_time, test_attempt.user) 
    str_date = date.strftime('%d %B, %Y')
    str_len = len(str_date)
    str_width = p.stringWidth(str_date, 'BebasNeue', 35)
    
    p.setFont("BebasNeue", 35)
    x = 369-int(str_width/2)
    p.drawString(x, 170, str_date)
    
    #Draw Certification Code
    str_len = len(cert_code)
    p.setFont("Times-Roman", 12)
    str_width = p.stringWidth(cert_code, "Times-Roman", 12)
    x = 155-int(str_width/2)
    p.drawString(x, 60, cert_code)  
    
    code = unicode("HHLEARN® Double QR Secure Certificate of Completion™\n\n", 'utf-8') + "ID: " + cert_code + "\n\n" + test_attempt.user.first_name + " " + test_attempt.user.last_name + "\nCompleted: " + course_name + "\nOn: " + str_date 
    #code = unicode("HHLEARN Double QR Secure Certificate of Completion", 'utf-8') + "Secure ID: " + cert_code + " Robert Thompson" + " Completed: " + course_name + "\nOn: " + str_date
    
    url = 'https://www.hhlearn.com/scoc/' + cert_code_encrypted
    qr_code_url = "http://chart.apis.google.com/chart?" + urllib.urlencode({'chs':'200x200', 'chld':'|0', 'cht':'qr', 'chl':url, 'choe':'UTF-8'})
    fd = urllib2.urlopen(qr_code_url) 
    image_file = StringIO.StringIO(fd.read()) 
    im = PIL.Image.open(image_file) 
    
    #Set fill color and stroke color
    p.setStrokeColorRGB(255, 255, 255)
    p.setFillColorRGB(255, 255, 255)        
    # draw a white border
    p.rect(160, 75, 80, 80, fill=1)
    #draw qrcode image
    p.drawInlineImage(im, 170, 85, width=60, height=60)
      
    qr_code_url = "http://chart.apis.google.com/chart?" + urllib.urlencode({'chs':'200x200', 'cht':'qr', 'chld':'|0', 'chl':code.encode('utf-8'), 'choe':'UTF-8'})
    fd = urllib2.urlopen(qr_code_url) 
    image_file = StringIO.StringIO(fd.read()) 
    im = PIL.Image.open(image_file)
    
    # draw a white border
    p.rect(70, 75, 80, 80, fill=1)
         
    p.drawInlineImage(im, 80, 85, width=60,height=60)
    
    #draw copyright string
    #p.setStrokeColorRGB(float(78)/255, float(87)/255, float(89)/255)
    p.setFont("Times-Roman", 12)
    p.setFillColorRGB(float(78)/255, float(87)/255, float(89)/255)
    #copyright_string = unicode('© 2013-', 'utf-8') + str(date.year) + ' Dynamic Agenda, Inc. All rights reserved. HHLEARN, HHLEARN logo, and Double QR are registered trademarks.'
    cur_year = datetime.now()
    copyright_string = unicode('© 2013-', 'utf-8') + str(cur_year.year) + unicode(' Dynamic Agenda, Inc. All rights reserved. Certificate with Double QR™ Technology is Patent-Pending.', 'utf-8')
    p.drawString(80, 45, copyright_string.encode('utf-8'))
    
    
    #set author and title for this pdf
    p.setAuthor('Dynamic Agenda, Inc.')
    p.setTitle(unicode('HHLEARN® Double QR Secure Certificate of Completion™','utf-8'))
    p.setSubject('Double QR Secure Certificate of Completion')

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    
    return response

def coord(x, y, height, unit=1):
    x, y = x * unit, height -  y * unit
    return x, y

def certificate_report(request, cert_code_encrypted=None):
        
    #get test attempt object
    cert_code = base64.urlsafe_b64decode(str(cert_code_encrypted))
    
    test_attempt_id = None
    try:    
        test_attempt_id = decryptnumber(cert_code[:13])
    except:
        try:
            test_attempt_id = decryptnumber(cert_code[:12])
        except:
            try:
                test_attempt_id = decryptnumber(cert_code[:11])
            except:
                try:
                    test_attempt_id = decryptnumber(cert_code[:10])
                except:
                    try:
                        test_attempt_id = decryptnumber(cert_code[:9])
                    except:
                        return render(request, 'pages/404.html', {'request': request})
    
    if test_attempt_id is not None:
        try:
            test_attempt = CoreTestAttempts.objects.get(id=test_attempt_id)
        except CoreTestAttempts.DoesNotExist:
            return render(request, 'pages/404.html', {'request': request})
    """
    pdfmetrics.registerFont(TTFont('BebasNeue', settings.STATIC_ROOT+'fonts/bebasneue-webfont.ttf'))
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="' + cert_code + '.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    p.drawImage(settings.STATIC_ROOT+'dashboard/certificate/images/bk_course_additional_documentation_report.png', 0,0, width=21.59*cm,height=27.94*cm,mask=None)
    p.setPageSize((21.59*cm,  27.94*cm))
    
    width = 21.59*cm 
    height = 27.94*cm
    
    t = p.beginText()
    #t.setFont('Arial', 25)
    #t.setCharSpace(3)    
    #t.setTextOrigin(159,782)    
    #t.textLine()
    styles = getSampleStyleSheet()
    text = Paragraph(test_attempt.test.course.long_description,
              styles['Normal'])
    text.wrapOn(p, width-50, height)    
    text.drawOn(p, 20, 600)
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()    
    """
    #get course objectives
    objectives = test_attempt.test.course.objectives.all()
    objectives_data = []
    for objective in objectives:
        objectives_data.append(replace_tags(request, objective.description))
        
    #get authors data
    author_info = CoreCourseAuthorQualifications.objects.get(courses=test_attempt.test.course)
    #author_info = CoreCourseAuthorQualifications.objects.get(courses_id=9)
    course_description = replace_tags(request, test_attempt.test.course.long_description)
    
    #generate verification code
    cur_year = convert_timezone(test_attempt.grade_date_time,  test_attempt.user)
    tt = cur_year.timetuple()  
    verification_code = base64.b64encode(str(test_attempt.test.course.id))+':'\
                        +base64.b64encode(str(test_attempt.test.course.monthly_safety_course.value))+':'\
                        +base64.b64encode(str(test_attempt.assignment_id))
    verification_code = verification_code + str(test_attempt.user.id) + "-"\
                         + str(test_attempt.assignment_id) + "-"\
                         + str(tt.tm_yday)
    
    #create qrcode images
    course_name = test_attempt.test.course.name
    #date = test_attempt.start_time + timedelta(seconds=test_attempt.seconds_taken)
    date = convert_timezone(test_attempt.grade_date_time, test_attempt.user)     
    str_date = date.strftime('%d %B, %Y')
    code = unicode("HHLEARN® Double QR™ Secure Additional Documentation\n\n", 'utf-8') + "Verification ID: " + verification_code + "\n\n" + test_attempt.user.first_name + " " + test_attempt.user.last_name + "\nCourse: " + course_name + "\nCompleted: " + str_date 
    #code = unicode("HHLEARN Double QR Secure Certificate of Completion", 'utf-8') + "Secure ID: " + cert_code + " Robert Thompson" + " Completed: " + course_name + "\nOn: " + str_date
    
    url = 'https://www.hhlearn.com/scocd/' + cert_code_encrypted
    qr_code_url = "http://chart.apis.google.com/chart?" + urllib.urlencode({'chs':'200x200', 'chld':'|0', 'cht':'qr', 'chl':url, 'choe':'UTF-8'})
    fd = urllib2.urlopen(qr_code_url) 
    image_file = StringIO.StringIO(fd.read()) 
    im = PIL.Image.open(image_file)
    im.save(settings.STATIC_ROOT+"temp/qr2.png")
    
    qr_code_url = "http://chart.apis.google.com/chart?" + urllib.urlencode({'chs':'200x200', 'cht':'qr', 'chld':'|0', 'chl':code.encode('utf-8'), 'choe':'UTF-8'})
    fd = urllib2.urlopen(qr_code_url) 
    image_file = StringIO.StringIO(fd.read()) 
    im = PIL.Image.open(image_file)
    im.save(settings.STATIC_ROOT+"temp/qr1.png")
      
    #generate copyright string
    
    copyright_string = unicode('© 2013-', 'utf-8') + str(cur_year.year) + unicode(' Dynamic Agenda, Inc, All rights reserved. Double QR™ Technology is Patent-Pending.', 'utf-8')    
    
    t = get_template('dashboard/certificate/rml_course_regulatory_document.html')
    c = Context({"user": request.user,
                 "test": test_attempt,
                 "course_description": course_description, 
                 "objectives": objectives_data,
                 "author_info": author_info,
                 "copyright": copyright_string,
                 "verification_code": verification_code,
                 "test_completed_date": date
                 })
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

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
    

'''
    Demo cert code
'''
DEMO_CERT = ['G09PK7BYH0AZZPW63H134FA', 'I2ML1S5J389SBW3E5KAZP23D', 'RHH06Q29L6E39ANX1D8K23M', 'B234567890X4SH67KL55FWQG', 'MZJUSUVJQJNASKRAWDNKTDFH']
DEMO_CERT_DATA = {'G09PK7BYH0AZZPW63H134FA' : {'cert_id' : 'G09PK7BYH0AZZPW63H134FA',
                                              'user_name' : 'Gwen Tofanelli',
                                              'course_name' : 'Home Health Aide Competency Examination',
                                              'end_date' : '1 June, 2012' },
                  'I2ML1S5J389SBW3E5KAZP23D' : { 'cert_id' : 'I2ML1S5J389SBW3E5KAZP23D',
                                               'user_name' : 'Benjamin Garcia',
                                               'course_name' : 'Company Policy Compliance',
                                               'end_date' : '1 June, 2012' },
                  'RHH06Q29L6E39ANX1D8K23M' : { 'cert_id' : 'RHH06Q29L6E39ANX1D8K23M',
                                                'user_name' : 'James R. Andersen',
                                                'course_name' : 'Biologic Exposure Management',
                                                'end_date' : '1 June, 2012'},
                  'B234567890X4SH67KL55FWQG' : { 'cert_id' : 'B234567890X4SH67KL55FWQG',
                                                'user_name' : 'Stephanie Hoffman',
                                                'course_name' : 'Introduction to HHLEARN',
                                                'end_date' : '1 June, 2012'},
                  'MZJUSUVJQJNASKRAWDNKTDFH' : { 'cert_id' : 'MZJUSUVJQJNASKRAWDNKTDFH',
                                                'user_name' : 'John Q. Public',
                                                'course_name' : 'Introduction to HHLEARN',
                                                'end_date' : '1 June, 2014'},                 
                  }
"""
    This function will be performed when user scan qr code image
"""
def verficiation(request, cert_code_encrypted=None):
    test_attempt_id = None
    if cert_code_encrypted in DEMO_CERT:
        return render(request, 'dashboard/certificate/verification.html', {'request': request, 'testAttemptId': cert_code_encrypted})
    try:
        #get test attempt object
        cert_code = base64.urlsafe_b64decode(str(cert_code_encrypted))
        test_attempt_id = decryptnumber(cert_code[:13])
    except:
        try:
            test_attempt_id = decryptnumber(cert_code[:12])
        except:
            try:
                test_attempt_id = decryptnumber(cert_code[:11])
            except:
                try:
                    test_attempt_id = decryptnumber(cert_code[:10])
                except:
                    try:
                        test_attempt_id = decryptnumber(cert_code[:9])
                    except:
                        #return render(request, 'pages/404.html', {'request': request})
                        pass    
    
    try:
        test_attempt = CoreTestAttempts.objects.get(id=test_attempt_id)
    except CoreTestAttempts.DoesNotExist:
        return render(request, 'dashboard/certificate/verification.html', {'request': request, 'testAttemptId': cert_code_encrypted})    
    
    return render(request, 'dashboard/certificate/verification.html', {'request': request, 'testAttemptId': test_attempt.id})

def verficiation_additional(request, cert_code_encrypted=None):
    test_attempt_id = None
    if cert_code_encrypted in DEMO_CERT:
        return render(request, 'dashboard/certificate/verification.html', {'request': request, 'testAttemptId': cert_code_encrypted, 'additional':1})
    try:
        #get test attempt object
        cert_code = base64.urlsafe_b64decode(str(cert_code_encrypted))
        test_attempt_id = decryptnumber(cert_code[:13])
    except:
        try:
            test_attempt_id = decryptnumber(cert_code[:12])
        except:
            try:
                test_attempt_id = decryptnumber(cert_code[:11])
            except:
                try:
                    test_attempt_id = decryptnumber(cert_code[:10])
                except:
                    try:
                        test_attempt_id = decryptnumber(cert_code[:9])
                    except:
                        #return render(request, 'pages/404.html', {'request': request})
                        pass    
    
    try:
        test_attempt = CoreTestAttempts.objects.get(id=test_attempt_id)
    except CoreTestAttempts.DoesNotExist:
        return render(request, 'dashboard/certificate/verification.html', {'request': request, 'testAttemptId': cert_code_encrypted, 'additional':1})    
    
    return render(request, 'dashboard/certificate/verification.html', {'request': request, 'testAttemptId': test_attempt.id, 'additional':1})


def result(request):
    post_data = request.POST
    
    if len(post_data.keys()) == 0:
        return render(request, 'pages/404.html', {'request': request})
        #raise Http404
    additional = post_data['additional']
    if additional:   
        additional = int(additional)
    #certification data for demos
    if post_data['testAttemptId'] in DEMO_CERT:
        cert_data = DEMO_CERT_DATA[post_data['testAttemptId']]
        return render(request, 'dashboard/certificate/demo_result.html', {'request': request, 'cert_data': cert_data, 'additional': additional})
    
 
                         
    #Get test attempt
    try:
        test_attempt_id = int(post_data['testAttemptId'])
    except:
        return render(request, 'dashboard/certificate/result.html', {'request': request, 'test_attempt_code': post_data['testAttemptId']})
    try:        
        test_attempt = CoreTestAttempts.objects.get(id=int(post_data['testAttemptId']))
                                     
    except CoreTestAttempts.DoesNotExist:
        return render(request, 'dashboard/certificate/result.html', {'request': request, 'test_attempt_code': post_data['testAttemptId']})
    
    #Get end date of test attempt
    #date = test_attempt.start_time + timedelta(seconds=test_attempt.seconds_taken)
    date = convert_timezone(test_attempt.grade_date_time, test_attempt.user) 
    str_date = date.strftime('%d %B, %Y')
    
    if additional:
        #generate verification code
        cur_year = convert_timezone(test_attempt.grade_date_time,  test_attempt.user)
        tt = cur_year.timetuple()  
        verification_code = base64.b64encode(str(test_attempt.test.course.id))+':'\
                            +base64.b64encode(str(test_attempt.test.course.monthly_safety_course.value))+':'\
                            +base64.b64encode(str(test_attempt.assignment_id))
        verification_code = verification_code + str(test_attempt.user.id) + "-"\
                             + str(test_attempt.assignment_id) + "-"\
                             + str(tt.tm_yday)
        return render(request, 'dashboard/certificate/result.html', {'request': request, 'test_attempt': test_attempt, 'end_date':str_date, 'verification_code': verification_code, 'additional': additional})
    
    return render(request, 'dashboard/certificate/result.html', {'request': request, 'test_attempt': test_attempt, 'end_date':str_date})
