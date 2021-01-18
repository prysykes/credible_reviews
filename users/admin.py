from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from users.forms import ReviewForm

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
admin.site.register(UserProfile, UserProfileAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('company', 'subject', 'review_text', 'date_added')
    autocomplete_fields = ['company']
    form = ReviewForm

admin.site.register(Review, ReviewAdmin)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ['user', 'response']

admin.site.register(Response, ResponseAdmin)

class ResponseReplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'reply']

admin.site.register(ResponseReply, ResponseReplyAdmin)

class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'review', 'like_count']

admin.site.register(Like, LikeAdmin)


