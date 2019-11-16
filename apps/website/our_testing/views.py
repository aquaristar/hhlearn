from django.shortcuts import render
import datetime


def our_testing(request):
    now = datetime.datetime.now()
    return render(request, 'website/our_testing/index.html', {'request': request})

