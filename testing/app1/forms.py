from django import forms
from .models import User1
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):

    class Meta:
        model = User1
        fields= "__all__"

