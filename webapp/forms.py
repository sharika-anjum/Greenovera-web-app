from django import forms
from django.forms import ModelForm

from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = "__all__"