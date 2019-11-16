# -*- coding: utf-8 -*-
from django.shortcuts import render
import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from apps.api.v1.utils.helpers import *


def home(request):
    now = datetime.datetime.now()
    return render(request, 'home.html', {'request': request})

def milestones(request):
    now = datetime.datetime.now()
    return render(request, 'dashboard/milestones/index.html', {'request': request})

'''
def contactus(request):
    if 'email_address' in request.POST:    
        email_address = request.POST['email_address']    
        server_email = "rc_thompson@hhlearn.com"        
        subject = "Beta Sign-Up"
        message = """Thank you for contacting HHLEARN in regards to participating in our Beta+ project. We will be contacting you shortly to obtain additional information from you in regards to your organization.
    
Please be prepared to share with us the your organization’s number of locations, number of employees, which home health industry specialties are in your scope of care, and whether you are using a learning management system currently.
    
Thank you for showing interest in HHLEARN and we will communicate with you promptly.
    
Sincerely,

Robert C. Thompson, RCP, RN. PHN, BSN"""    
    
        msg = EmailMessage(subject, message, server_email, [email_address])
        msg.send()
        
        message = "Contact: " + email_address + "\nIP: " + get_client_ip(request)
        
        msg = EmailMessage(subject, message, email_address, [server_email])
        msg.send()         

    return render(request, 'pages/contact.html', {'request': request})
'''
