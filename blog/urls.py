from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    path('<slug:post_slug>/', views.post_detail, name='post_detail'),
    
    ]