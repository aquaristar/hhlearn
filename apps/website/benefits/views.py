from django.shortcuts import render
import datetime


def benefits(request):
    now = datetime.datetime.now()
    return render(request, 'website/benefits/index.html', {'request': request})

