from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'website','locations','sector_focus','stage','duration','deal','bio','logo')


# class Form(forms.ModelForm):
    
#     class Meta:
#         model = 
#         fields = ("",)
    