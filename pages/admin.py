from django.contrib import admin
from .models import NewsletterSignUp


class NewsletterSignUpAdmin(admin.ModelAdmin):
    list_display = ['email']


admin.site.register(NewsletterSignUp, NewsletterSignUpAdmin)