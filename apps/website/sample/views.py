from django.shortcuts import render
import datetime


def sample(request):
    now = datetime.datetime.now()
    return render(request, 'website/sample/index.html', {'request': request})
