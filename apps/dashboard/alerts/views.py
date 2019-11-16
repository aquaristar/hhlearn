from django.shortcuts import render
import datetime


def index(request):
    now = datetime.datetime.now()
    return render(request, 'dashboard/alerts/index.html', {'request': request})