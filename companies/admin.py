from django.contrib import admin
from . models import Company
# from companies.forms import ReviewForm


class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"company_slug": ("company_name",)} # a js helper to prepopulate a model field with another model field
    list_display = ('company_name', 'company_website', 'company_email', 'company_phone', 'package_chosen', 'approved')
    autocomplete_fields = ['user']
    search_fields = ["company_name"]

admin.site.register(Company, CompanyAdmin)

# Register your models here.
