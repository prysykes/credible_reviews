from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'post_slug': ('title',)}
    list_display = ['title', 'post_slug', 'status', 'created_on']
    list_filter = ('status',)
    search_fields = search_fields = ["title"]

admin.site.register(POST, PostAdmin)