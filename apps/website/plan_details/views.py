from django.shortcuts import render
import datetime


def plan_details(request):
    now = datetime.datetime.now()
    return render(request, 'website/plan_details/index.html', {'request': request})
