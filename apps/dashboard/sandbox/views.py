from django.shortcuts import render

def test_page(request):

    return render(request, 'dashboard/sandbox/test_page.html', {'request': request})

def sample1(request):
    return render(request, 'dashboard/sandbox/sample1.html', {'request': request})

def countdown(request):
    return render(request, 'dashboard/sandbox/countdown.html', {'request': request})