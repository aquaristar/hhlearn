from django.shortcuts import render
import datetime


def messages(request):
    now = datetime.datetime.now()
    return render(request, 'dashboard/messages/index.html', {'request': request})
