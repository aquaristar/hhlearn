from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from apps.dashboard.models import *
from apps.api.v1.utils.helpers import *

from datetime import datetime
import mailchimp
import json

from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage


def home(request):    
    #return render(request, 'website/home/index.html', {'request': request})
    #return render(request, 'dashboard/sandbox/countdown.html', {'request': request})
    return render(request, 'website/home/loginhome.html', {'request': request})

def old_home(request):    
    #return render(request, 'website/home/index.html', {'request': request})    
    return render(request, 'sandbox/loginhome.html', {'request': request})

def contacts(request):
    now = datetime.now()
    
    if 'email' in request.POST and request.POST['email']:
        email_address = request.POST['email']
        try:
            list = mailchimp.utils.get_connection().get_list_by_id('3393152033')
            list.subscribe(email_address, {'EMAIL': email_address})
        except Exception as e:
            response = {'status': 'error',
                        'message': e.message,
                       }
            return HttpResponse(json.dumps(response), content_type="application/json")
        
        response = {'status': 'success' }
        return HttpResponse(json.dumps(response), content_type="application/json")    
    
    return HttpResponseRedirect(reverse('home'))

#function to process contact us form in features page  
def contact_us(request):
    now = datetime.now()        
    if 'email' in request.POST and request.POST['email']:
        email_address = request.POST['email']
        try:
            #record contact info to db
            contact = CoreContactUs.objects.create(contact_full_name = request.POST['name'],
                                                contact_email = request.POST['email'],
                                                contact_company = request.POST['company'],
                                                contact_company_website = request.POST['website'],
                                                contact_ip_address = get_client_ip(request),
                                                contact_add_date = now,
                                                contact_message = request.POST['message'])
            '''
            #send email to mailchimp
            list = mailchimp.utils.get_connection().get_list_by_id('3393152033')
            list.subscribe(email_address, {'EMAIL': email_address, 
                                           'FNAME': request.POST['name'], 
                                           'CNAME': request.POST['company'],
                                           })
            '''
            #send mail to administrator
            email_message = 'User Name:' + request.POST['name'] + ' company : ' + request.POST['company'] + \
                            ' website:' + request.POST['website'] + ' message:' + request.POST['message']
            msg = EmailMessage('Contact Us Message',
                      email_message, to=['rc_thompson@me.com'])
            msg.send()
            #send verification email to contactor
            verification_msg = EmailMessage('Contact Us Message Sent',
                      'Your Verficiation Message is sent to HHLEARN administrator', to=[request.POST['email']])
            verification_msg.send()
        except Exception as e:
            response = {'status': 'error',
                        'message': e.message,
                       }
            return HttpResponse(json.dumps(response), content_type="application/json")
        
        response = {'status': 'success' }
        return HttpResponse(json.dumps(response), content_type="application/json")    
    
    return HttpResponseRedirect(reverse('home'))

#function to process newsletter form in features page
def contact_newsletter(request):
    if 'email' in request.POST and request.POST['email']:
        email_address = request.POST['email']
        try:
            '''
            #record contact info to db
            contact = CoreContactUs.objects.create(contact_full_name = request.POST['name'],
                                                contact_email = request.POST['email'],
                                                contact_company = request.POST['company'],
                                                contact_company_website = request.POST['website'],
                                                contact_ip_address = get_client_ip(request),
                                                contact_add_date = now,
                                                contact_message = request.POST['message'])
            '''
            #send email to mailchimp
            list = mailchimp.utils.get_connection().get_list_by_id('ebc29fbfd6')
            list.subscribe(email_address, {'EMAIL': email_address, 
                                           'FNAME': request.POST['first_name'],
                                           'LNAME': request.POST['last_name'], 
                                           'CNAME': request.POST['company'],
                                           'LMS': request.POST['newsletter_lms']},
                                           )
        except Exception as e:
            response = {'status': 'error',
                        'message': e.message,
                       }
            return HttpResponse(json.dumps(response), content_type="application/json")
        
        response = {'status': 'success' }
        return HttpResponse(json.dumps(response), content_type="application/json")    
    
    return HttpResponseRedirect(reverse('home'))
