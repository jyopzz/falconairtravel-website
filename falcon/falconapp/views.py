from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'index.html')

@login_required()
def admindash(request):
    return render(request, 'admindash.html')

@login_required()
def myprofile(request):
    return render(request,'myprofile.html')

@login_required()
def developer(request):
    return render(request,'developer.html')
    
