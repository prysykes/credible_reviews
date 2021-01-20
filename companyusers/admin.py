from django.contrib import admin
from .models import UserProfileCompany, Message, ReplyMessage



class UserProfileCompanyAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'designation']
    search_fields = ['rep_name']

admin.site.register(UserProfileCompany, UserProfileCompanyAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'subject', 'message']

admin.site.register(Message, MessageAdmin)

class ReplyMessageAdmin(admin.ModelAdmin):
    list_display = ['message', 'sender', 'reply']

admin.site.register(ReplyMessage, ReplyMessageAdmin)
