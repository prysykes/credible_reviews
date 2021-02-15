from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='blog'),
    path('<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('<int:comment_id>/', views.post_detail, name='reply_comment'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    
    ]