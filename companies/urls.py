from django.urls import path
from . import views


urlpatterns = [
    path('<slug:company_id>/', views.dynamic_url, name='detail'),
    
    ]
