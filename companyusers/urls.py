from django.urls import path
from . import views
from .views import CompanyVerificationView
from users.views import user_login

from django.contrib.auth import views as auth_views



urlpatterns = [
    path('sign-up-company', views.sign_up_company, name='sign-up-company'),
    path('profile_company', views.profile_company, name='profile_company'),
    path('request_review', views.request_review_api, name='request_review'),

    path('company_activation_view/<uidb64>/<token>', views.CompanyVerificationView.as_view(), name='company_activation_view'),
    
    path('logoutpage_company', views.logoutpage_company, name='logoutpage_company'),
    path('user_login', user_login, name='user_login'),
    path('done.html', views.done, name='done'),   
    path('settings_company', views.settings_company, name='settings_company'),
    path('response/<int:review_id>', views.response, name='response'),
    
    # overwriting the default template name for reset_password for company users
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="company_users/reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="company_users/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="company_users/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="company_users/password_reset_done.html"), name="password_reset_complete"),
    

    
]
