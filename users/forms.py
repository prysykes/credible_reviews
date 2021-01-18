from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

from companies.models import Company



class SignUpFormRegular(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'phone', 'location']
        exclude = ['user']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['company','subject', 'review_text', 'rating']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.none()

        if 'company' in self.data:
            self.fields['company'].queryset = Company.objects.all()
    
    
        
    

        
        

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['response']
