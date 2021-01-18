from django.contrib import admin
from . models import Company
# from companies.forms import ReviewForm


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_website', 'company_email', 'company_phone', 'package_chosen')
    autocomplete_fields = ['user']
    search_fields = ["company_name"]

admin.site.register(Company, CompanyAdmin)

# Register your models here.
