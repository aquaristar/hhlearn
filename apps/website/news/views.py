from django.shortcuts import render
import datetime


def news(request):
    now = datetime.datetime.now()
    return render(request, 'website/news/index.html', {'request': request})
