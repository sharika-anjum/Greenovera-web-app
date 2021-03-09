from django import forms
from .forms import *

from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = "__all__"