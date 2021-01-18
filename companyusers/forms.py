from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import  UserProfileCompany, Message, ReplyMessage


class SignUpFormCompany(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        

class UserProfileCompanyForm(ModelForm):
    class Meta:
        model = UserProfileCompany
        fields = ['designation', 'profile_photo', 'package', 'phone', 'location', 'address', 'phone']
        exclude = ['user']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'message']

class ReplyMessageForm(ModelForm):
    class Meta:
        model = ReplyMessage
        fields = ['reply']


