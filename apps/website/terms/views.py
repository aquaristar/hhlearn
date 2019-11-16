from django.shortcuts import render
import datetime


def terms(request):
    now = datetime.datetime.now()
    return render(request, 'website/terms/index.html', {'request': request})
