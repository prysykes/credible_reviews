from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='blog'),
    path('<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('<slug:post_slug>/<int:comment_id>/', views.reply_comment, name='reply_comment'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:reply_id>', views.delete_reply, name='delete_reply'),
    path('<int:comment_id>', views.delete_comment, name='delete_comment'),
    
    ]