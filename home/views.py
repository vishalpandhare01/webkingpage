from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
#username bisal pass@123
def index(request):
    return render(request,'index.html')

def reg(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']

        r=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
        r.save()
        print('user created')

        return redirect('index.html')
    return render(request,'auth/registration.html')

def login(request):
    if request.method=='POST':
        username =request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username,password=password)
        if user is not None:
            return redirect('home.html')
        else:
            return redirect('login.html')


    return render(request,'auth/login.html')
            

def home(request):
    return render(request,'home.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')    

