from django.forms import ModelForm
from .models import Company
from users.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']



class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'company_state', 'company_address', 'company_email', 'company_phone', 'company_website',  'company_sector', 'company_description', 'company_logo', 'sample_pics_one', 'sample_pics_two', 'sample_pics_three', 'sample_pics_four',  'package_chosen']
        



""" class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__' """