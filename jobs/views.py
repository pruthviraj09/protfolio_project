from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Job

# Create your views here.

def home(request):
    jobs=Job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})
def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('jobs/home.html')
        else:
            return render(request,'jobs/login.html',{'error':'username is wrong'})
    else:
        return render(request,'jobs/login.html')
def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            User1=User.objects.create_user(username=request.POST['username'],password='password1')
            auth.login(request,User1)
            return redirect('jobs/home.html')
    else:
        return render(request,'jobs/signup.html')
def logout(request):
    return render(request,'jobs/logout.html')
