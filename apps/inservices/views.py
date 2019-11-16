from django.shortcuts import render
from apps.dashboard.models import *
from apps.reporting.models import *

def index(request):
    
    return render(request, 'inservices/index.html', {'request': request})


