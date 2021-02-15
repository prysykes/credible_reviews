import django_filters
from companies.models import Company
from users.models import Review
from django import forms

class CompanyFilter(django_filters.FilterSet):
    company_name = django_filters.CharFilter(
        widget=forms.TextInput(attrs={'placeholder': 'Capfirst eg. Credible'})
    )
    class Meta:
        model = Company
        fields = [
            'company_name',
            'company_sector',
            'company_state',
            'average_rating',
        ]



class ReviewFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(
        widget=forms.TextInput(attrs={'class': 'form-control', 'size': '6', 'autocomplete': 'off', 'placeholder': 'type name to choose'})
    )
    
    class Meta:
        model = Review
        fields = [
            'company',
            'rating',
            'date_added',
        ]