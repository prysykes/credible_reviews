import django_filters
from companies.models import Company
from users.models import Review

class CompanyFilter(django_filters.FilterSet):
    class Meta:
        model = Company
        fields = [
            'company_name',
            'company_sector',
            'company_state',
            'average_rating',
        ]


class ReviewFilter(django_filters.FilterSet):
    class Meta:
        model = Review
        fields = [
            'company',
            'rating',
            'date_added',
        ]