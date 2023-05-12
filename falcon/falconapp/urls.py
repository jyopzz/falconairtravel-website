from django.urls import path
from . import views





urlpatterns = [
    #path to home page (index.html) starting
    path('', views.home, name='home'),
    #path to home page (index.html) ending

    #path to login page (adminlogin.html) starting
    path('dash/',views.admindash,name="dash"), #path to admindash 
    #path to login page (adminlogin.html) ending

    #path to admindash.html->myprofile.html; admindash.html->developer.html starting
    path('dash/mypro/',views.myprofile,name='mypro'),#path to myprofile 
    path('dash/deve/',views.developer,name='deve'),#path to developer
    #path to admindash.html->myprofile.html; admindash.html->developer.html ending
    
]