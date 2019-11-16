from django.shortcuts import render
import datetime


def documents(request):
    now = datetime.datetime.now()
    return render(request, 'dashboard/documents/index.html', {'request': request})
