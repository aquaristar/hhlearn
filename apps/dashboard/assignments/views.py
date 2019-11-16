from django.shortcuts import render
import datetime


def assignments(request):
    now = datetime.datetime.now()
    return render(request, 'dashboard/assignments/index.html', {'request': request})

