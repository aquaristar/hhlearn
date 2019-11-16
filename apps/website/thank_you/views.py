from django.shortcuts import render
import datetime


def thank_you(request):
    now = datetime.datetime.now()
    return render(request, 'website/thank_you/index.html', {'request': request})
