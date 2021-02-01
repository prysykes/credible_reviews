from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'post_slug': ('title',)}
    list_display = ['title', 'post_slug', 'status', 'created_on']
    list_filter = ('status',)
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'content')

admin.site.register(Comment, CommentAdmin)