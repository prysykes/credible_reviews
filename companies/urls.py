from django.urls import path
from . import views


urlpatterns = [
    path('<int:company_id>/', views.dynamic_url, name='detail'),
    
    ]
