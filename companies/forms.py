from django.forms import ModelForm
from .models import *
from users.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']


""" class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__' """