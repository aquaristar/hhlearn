from django.shortcuts import render
import datetime


def reporting(request):
    now = datetime.datetime.now()
    return render(request, 'website/reporting/index.html', {'request': request})
