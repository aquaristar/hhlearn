from django.shortcuts import render
import datetime


def demos(request):
    now = datetime.datetime.now()
    return render(request, 'website/demos/index.html', {'request': request})
