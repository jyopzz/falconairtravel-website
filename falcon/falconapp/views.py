from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Addreview

def home(request):
    return render(request, 'index.html')

@login_required()
def admindash(request):
    return render(request, 'admindash.html')

@login_required()
def myprofile(request):
    return redirect('password_change')

@login_required()
def developer(request):
    return render(request,'developer.html')
    
@login_required()
def addreview(request):
    if request.method=="POST":
        name=request.POST.get('name')
        image=request.FILES['img']
        designation=request.POST.get('desig')
        message=request.POST.get('message')
        print(name,image,designation,message)
        addreobj=Addreview()
        addreobj.name=name
        addreobj.image=image
        addreobj.designation=designation
        addreobj.message=message
        addreobj.save()
        return redirect('dash')

    return render(request,'addreview.html')

@login_required()
def removereview(request):
    return render(request,'rmreview.html')

@login_required()
def updatereview(request):
    return render(request,'upreview.html')

