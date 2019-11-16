from django.shortcuts import render
import datetime


def our_modules(request):
    now = datetime.datetime.now()
    return render(request, 'website/our_modules/index.html', {'request': request})
