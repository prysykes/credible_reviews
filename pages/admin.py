from django.contrib import admin
from .models import NewsletterSignUp, Ads


class NewsletterSignUpAdmin(admin.ModelAdmin):
    list_display = ['email']


admin.site.register(NewsletterSignUp, NewsletterSignUpAdmin)


class AdsAdmin(admin.ModelAdmin):
    list_display = ['ad_name', 'ad_url']
    
admin.site.register(Ads, AdsAdmin)