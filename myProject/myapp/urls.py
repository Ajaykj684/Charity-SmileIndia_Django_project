from django.urls import path
from . import views



urlpatterns = [ 
    
     path('',views.Home,name='home'),
     path('about/',views.About,name='about'),
     path('donate',views.Donate,name='donate'),
     path('contactPage',views.ContactPage,name='contactPage'),
     path('mission',views.Mission,name='mission'),
     path('news',views.News,name='news'),
     path('signup',views.Signup,name='signup'),
     path('login',views.Login,name='login'),
     path('logout',views.Logout,name='logout'),
     path('contactform',views.contactform,name='contactform'),
     path('payment',views.Payment,name='payment'),
     path('payment_successfull',views.Payment_successfull,name='payment_successfull'),
     path('Readmore',views.Readmore,name='Readmore'),
     path('transparency',views.Transparency,name='transparency'),






     




]