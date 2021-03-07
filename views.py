from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from django.contrib import messages, auth
# Create your views here.
from .models import User1


def base_view(request):
    return render(request, "base.html")

def index_view(request):
    return render(request, "index.html")


def register_1(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../test/base")

    else:
        form=UserForm()
    return render(request,"register1.html",{"form":form})


def register_2(request):
    if request.POST.get("register"):
        if request.method=="POST":
            if request.get.method()=="register":

                form = UserForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect("../test/base")
    else:
        form=UserForm()
    return render(request,"index.html",{"form":form})


def login_1(request):
    return render(request,"login.html")
def log_ch1(request):
    if request.POST.get("login"):
        if request.method=="POST":
                email=request.POST['email']
                password=request.POST['password']
                try:
                    u= User1.objects.get(email=email,password=password)
                    if u is not None:
                        return render(request,"base.html",{"u":u})
                    else:
                        messages.info(request,'invalid')
                        return redirect('../test/login')
                except:
                    messages.info(request,'invalid')
                    return redirect("../test/login")
        else:
            return render(request,'login.html')