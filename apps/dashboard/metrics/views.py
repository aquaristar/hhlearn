from django.shortcuts import render
import datetime


def metrics(request):
    now = datetime.datetime.now()
    return render(request, 'dashboard/metrics/index.html', {'request': request})
