from django.shortcuts import render
import datetime


def choose_edition(request):
    now = datetime.datetime.now()
    return render(request, 'website/choose_edition/index.html', {'request': request})
