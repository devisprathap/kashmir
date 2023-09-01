from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse


def  register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email= request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('/register')
            else:

                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('/login')
        else:
            messages.info(request,'password not matching')
            return redirect('/register')
        return redirect('/')

    return render(request,"register.html")





def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credential")
            return redirect('login')
    return render(request,"login.html")









def form(request):
    return render(request,"form.html")
def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

def home(request):
    return render(request,"home.html")
def link(request):
    return render(request,"link.html")
    return redirect('/')