from django.shortcuts import render

# Create your views here.


def Index(request):
    return render(request, 'index.html')


def UserProfile(request):
    return render(request, 'userprofile.html')
