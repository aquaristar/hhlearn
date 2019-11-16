from django.shortcuts import render
import datetime


def privacy(request):
    now = datetime.datetime.now()
    return render(request, 'website/privacy/index.html', {'request': request})
