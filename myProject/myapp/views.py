from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib import messages,auth
from .models import DonateContact,Contact,Donation,Message
from django.http import HttpResponse,JsonResponse
from datetime import datetime
import datetime
import json
# Create your views here.


def Home(request):
    return render(request,'Home.html')

def About(request):
    return render(request,'about.html')

def Donate(request):
    return render(request,'donate.html')

def ContactPage(request):
    if request.method == 'POST':
        user = request.user
        name =  request.POST['Name']
        email =  request.POST['Email']
        phone =  request.POST['Phone']
        message =  request.POST['Message']
        Contact.objects.create(user= user , name= name ,email =email, phone = phone,message= message )
        messages.success(request,'Happy to see your interest, we will contact you soon,thank you  !')

        return redirect('home')

    return render(request,'contact.html')

def Mission(request):
    return render(request,'mission.html')


def News(request):
    return render(request,'news.html')


def Signup(request):
    if request.method == "POST":
        firstname =  request.POST['First_name']
        lastname =  request.POST['Last_name']
        email =  request.POST['email']
        password =  request.POST['password']
        User.objects.create_user(first_name = firstname , last_name = lastname, email=email, password = password ,username = email)
        messages.success(request,'Registered Succesfully !')
        return render(request,'signup.html')
    else : 
        return render(request,'signup.html')



def Login(request):
    if request.method == 'POST':
        email =  request.POST['UserEmail']
        password =  request.POST['UserPassword']

        user = auth.authenticate(username=email, password=password)
    
        if user is not None:
            if user.is_active == True :
                auth.login(request,user)
                
                return redirect('home')  
            else:
           
                return redirect('login')  
        else:
            
            messages.error(request,'invalid credentials')
            return render(request,'signup.html') 
    else : 
    
        return render(request,'signup.html')
    
def Logout(request):
   
    auth.logout(request)
    
    return redirect('login')


def contactform(request):
    if request.method == 'POST':

        user = request.user
        name =  request.POST['Name']
        email =  request.POST['Email']
        phone =  request.POST['Phone']
        DonateContact.objects.create(user= user , name= name ,email =email, phone = phone)
        messages.success(request,'Happy to see your interest, we will contact you soon,thank you  !')

        return redirect('home')


def Paymentproceed(request):
    if request.method == "POST":
        category =  request.POST['category']
        



def Payment(request):
    if request.method == "POST":
            
        payment_id = str(int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
        body = json.loads(request.body)
        Category = body['category']
    
        user = request.user
        amount = 2000
        payment_method = 'Paypal'
        place = "usa"
        Donation.objects.create(payment_id=payment_id,Category=Category,user=user,amount=amount,payment_method=payment_method,place=place)
    
        return JsonResponse({'completed':'success'})



def Payment_successfull(request):
    return HttpResponse("<h1>Success</h1>")


def Readmore(request):
    return render(request,'Readmore.html')


def Transparency(request):
    donation = Donation.objects.all().order_by()[:5]

    return render(request,'Transparency.html',{ "donation" : donation })


def Reviews(request):
    message = Message.objects.all().order_by('-id')[:5]
    return render(request,'reviews.html',{"message": message})
    

def Comment(request):
    if request.method == "POST":
        msg =  request.POST['msg']
        Message.objects.create(user=request.user , message=msg)
    return redirect('reviews')
    


def viewComments(request):
    message = Message.objects.all()
    return render(request,'reviews.html',{"message": message})
    