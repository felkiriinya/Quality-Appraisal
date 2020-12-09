from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company,Review
from django.forms import ModelForm, Textarea

class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'website','locations','sector_focus','stage','duration','deal','bio','logo')

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'feedback','mentorship','hiring','community','fundraising','corporate_development')        
        widgets = {
            'title': Textarea(attrs={'cols': 60, 'rows': 1}),
            'feedback': Textarea(attrs={'cols': 60, 'rows': 15}),
            # 'mentorship': forms.RadioSelect,
            # 'hiring': forms.RadioSelect,
            # 'community': forms.RadioSelect,
            # 'fundraising': forms.RadioSelect,
            # 'corporate_development': forms.RadioSelect,
        }

