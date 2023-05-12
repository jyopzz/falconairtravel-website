from django.urls import path
from . import views





urlpatterns = [
    #path to home page (index.html) starting
    path('', views.home, name='home'),
    #path to home page (index.html) ending

    #path to login page (adminlogin.html) starting
    path('dash/',views.admindash,name="dash"), #path to admindash 
    #path to login page (adminlogin.html) ending

    #path from admindash.html->myprofile.html; admindash.html->developer.html; admindash.html->addreview.html; admindash.html->rmreview.html; admindash.html->upreview.html; tarting
    path('dash/mypro/',views.myprofile,name='mypro'),#path to myprofile 
    path('dash/deve/',views.developer,name='deve'),#path to developer
    path('dash/addre/',views.addreview,name='addre'),#path to addreview
    path('dash/rmre/',views.removereview,name='rmre'),#path to removereview
    path('dash/upre/',views.updatereview,name='upre'),#path to updatereview
    #path from admindash.html->myprofile.html; admindash.html->developer.html; admindash.html->addreview.html; admindash.html->rmreview.html; admindash.html->upreview.html; ending
    

    
]