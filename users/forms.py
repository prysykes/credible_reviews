from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User
from .models import *

from companies.models import Company



class SignUpFormRegular(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    # def clean(self):
    #         email = self.cleaned_data.get('email')
    #         if User.objects.filter(email=email).exists():
    #                 raise ValidationError("Email exists")
    #         return self.cleaned_data

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'phone', 'location']
        exclude = ['user']
        

class GenericReviewForm(ModelForm):
    class Meta:
        model = GenericReview
        fields = ['company_name_g', 'subject_g', 'review_text_g', 'rating_g', 
                    'company_logo_g', 'picture_evidence_g', 'company_sector_g', 'company_state_g',
                    'company_address_g', 'company_website_g', 'company_email_g', 'company_phone_g' 
                
                ]
        

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'review_text', 'rating']
    
    
    
class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['response']
