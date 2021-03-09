from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages,auth

from .models import *
from .forms import *

from .models import *
from .forms import *
# Create your views here.
def land(request):
    return render(request,"land.html")

def open(request):
    return render(request,"index.html")

def check(request):

    if request.method=='POST' and 'Sign up' in request.POST:
        form=UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('')
            except:
                pass
    else:
        form=UserForm()
    return render(request,'index.html',{'form':form})

def log_check(request):
    if request.method=="POST" and 'Login' in request.POST:

        name = request.POST['name']
        pwd = request.POST['pwd']
        try:
            u=user.objects.get(name=name,pwd=pwd)
            if u is not None:
                return redirect("home/")


            else:
                messages.info(request,'INVALID CREDENTIALS!')
                return redirect('/')
        except:
            messages.info(request, 'INVALID CREDENTIALS!')
            return redirect('/')
    else:
        return render(request,'login.html')