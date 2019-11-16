from django.shortcuts import render
import datetime


def pricing(request):
    now = datetime.datetime.now()
    return render(request, 'website/pricing/index.html', {'request': request})
