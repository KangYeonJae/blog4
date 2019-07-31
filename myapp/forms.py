from django import forms
from .models import Myapp
from django.forms import ModelForm


class MyappForm(forms.ModelForm):
    class Meta:
        model=Myapp
        fields=['title', 'body']