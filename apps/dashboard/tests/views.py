from django.shortcuts import render

def test(request, test_code_encrypted=None):
    return render(request, 'dashboard/tests/index.html', {'request': request})

def test_result(request, test_attempt_code_encrypted=None):
    return render(request, 'dashboard/tests/result.html', {'request': request})

