from django.shortcuts import render

def index(request, course_code_encrypted=None):
    return render(request, 'dashboard/tasks/index.html', {'request': request})

