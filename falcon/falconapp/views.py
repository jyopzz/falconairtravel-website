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
    
@login_required()
def addreview(request):
    return render(request,'addreview.html')

@login_required()
def removereview(request):
    return render(request,'rmreview.html')

@login_required()
def updatereview(request):
    return render(request,'upreview.html')