from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages,auth

from .models import *
from .forms import *
# Create your views here.
def land(request):
    return render(request,"land.html")

def open(request):
    return render(request,"index.html")

