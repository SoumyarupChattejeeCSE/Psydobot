from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
from django.http import HttpResponse


def login(request):
    return render(request,'login.html')


def index(request):
    return render(request,'start.html')


def signup(request):
    if(request.method=="POST"):
        if (len(request.POST['zip']) == 6):
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'login.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
                auth.login_1(request,user)
                return redirect('index')
        else:
            return render (request,'login.html', {'error':'ZIP Code is invalid!'})
    else:
        return render(request,'login.html')


def login_1(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
         
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index')

def home(request):
    return render(request,'home.html')

def stress(request):
    return render(request,'stress_meter.html')

def lowstress(request):
    return render(request,'low_stress.html')

def highstress(request):
    return render(request,'high_stress.html')

def moderatestress(request):
    return render(request,'moderate_stress.html')

def map(request):
    return render(request,'map.html')