from django.shortcuts import render
import datetime


def compliance(request):
    now = datetime.datetime.now()
    return render(request, 'website/compliance/index.html', {'request': request})
