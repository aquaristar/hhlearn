from django.shortcuts import render


# this will load view for dashboard homepage.
def home(request):
    return render(request, 'dashboard/profile/index.html', {'request': request})

def view(request):
    return render(request, 'dashboard/profile/view.html', {'request': request})



