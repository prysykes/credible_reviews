from django import forms
from django.forms import ModelForm
from .models import NewsletterSignUp

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)


class NewsletterForm(ModelForm):
    class Meta:
        model = NewsletterSignUp
        fields = ['email']