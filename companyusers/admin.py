from django.contrib import admin
from .models import UserProfileCompany



class UserProfileCompanyAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'designation']
    search_fields = ['rep_name']

admin.site.register(UserProfileCompany, UserProfileCompanyAdmin)
