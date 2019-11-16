from django.shortcuts import render
import datetime


def testimonials(request):
    now = datetime.datetime.now()
    return render(request, 'website/testimonials/index.html', {'request': request})

