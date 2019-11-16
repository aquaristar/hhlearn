from django.shortcuts import render
import datetime


def login(request):
    now = datetime.datetime.now()
    return render(request, 'website/login/index.html', {'request': request})
