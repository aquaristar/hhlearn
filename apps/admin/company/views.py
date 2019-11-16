from django.shortcuts import render
import datetime


def home(request):
    now = datetime.datetime.now()
    return render(request, 'dashboard/admin/company/index.html', {'request': request})
