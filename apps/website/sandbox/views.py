from django.shortcuts import render

def test_page(request):

    return render(request, 'dashboard/sandbox/test_page.html', {'request': request})

def loginhome(request):
    return render(request, 'sandbox/loginhome.html', {'request': request})

def features(request):
    return render(request, 'sandbox/features.html', {'request': request})

def features_page2(request):
    return render(request, 'sandbox/page2.html', {'request': request})

def features_page3(request):
    return render(request, 'sandbox/page3.html', {'request': request})

def features_page4(request):
    return render(request, 'sandbox/page4.html', {'request': request})

def features_page5(request):
    return render(request, 'sandbox/page5.html', {'request': request})

def faqs(request):
    return render(request, 'sandbox/faqs.html', {'request': request})

def other_book(request):
    return render(request, 'sandbox/other_book.html', {'request': request})

def terms(request):
    return render(request, 'sandbox/terms.html', {'request': request})

def countdown(request):
    return render(request, 'sandbox/countdown.html', {'request': request})

def signup_step1(request):
    return render(request, 'sandbox/signup/step1.html', {'request': request})

def signup_step2(request):
    return render(request, 'sandbox/signup/step2.html', {'request': request})

def signup_step3(request):
    return render(request, 'sandbox/signup/step3.html', {'request': request})

def signup_step4(request):
    return render(request, 'sandbox/signup/step4.html', {'request': request})

def page811(request):
    return render(request, 'sandbox/811.html', {'request': request})

