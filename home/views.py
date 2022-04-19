from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
#username bisal pass@123
def index(request):
    return render(request,'index.html')
            
def home(request):
    return render(request,'home.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')    

