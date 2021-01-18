from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *



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
        fields = ['company', 'review_text', 'rating']

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['response']
