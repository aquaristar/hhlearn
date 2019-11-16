from django.shortcuts import render
import datetime


def courses(request):
    now = datetime.datetime.now()
    return render(request, 'website/courses/index.html', {'request': request})
