from django.shortcuts import render
import datetime


def plans(request):
    now = datetime.datetime.now()
    return render(request, 'website/plans/index.html', {'request': request})
