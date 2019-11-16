from django.shortcuts import render
import datetime


def history(request):
    now = datetime.datetime.now()
    return render(request, 'dashboard/history/index.html', {'request': request})

