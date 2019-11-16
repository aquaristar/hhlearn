from django.shortcuts import render
import datetime


def contact(request):
    now = datetime.datetime.now()
    return render(request, 'website/contact/index.html', {'request': request})
