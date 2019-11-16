from django.shortcuts import render
import datetime


def code_of_conduct(request):
    now = datetime.datetime.now()
    return render(request, 'website/code_of_conduct/index.html', {'request': request})

