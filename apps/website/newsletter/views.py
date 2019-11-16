from django.shortcuts import render
import datetime


def newsletter(request):
    now = datetime.datetime.now()
    return render(request, 'website/newsletter/index.html', {'request': request})
