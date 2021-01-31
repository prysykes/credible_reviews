from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from users.forms import ReviewForm, GenericReviewForm

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
admin.site.register(UserProfile, UserProfileAdmin)

class GenericReviewAdmin(admin.ModelAdmin):
    list_display = ('user_g', 'company_name_g', 'subject_g', 'review_text_g', 'date_added_g')
    autocomplete_fields = ['user_g']
    form = GenericReviewForm

admin.site.register(GenericReview, GenericReviewAdmin)


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


class FlagAdmin(admin.ModelAdmin):
    list_display = ['user', 'review', 'flag_count']

admin.site.register(Flag, FlagAdmin)


