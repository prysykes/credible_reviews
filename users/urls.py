from django.urls import path
from . import views

from django.contrib.auth import views as auth_views



urlpatterns = [
    path('sign_up', views.sign_up, name='sign-up'),
    
   
    path('profile_regular', views.profile_regular, name='profile_regular'),
    
    path('logoutpage_regular', views.logoutpage_regular, name='logoutpage_regular'),
    
    path('user_login', views.user_login, name='user_login'),
    path('response_user/<int:review_id>', views.response_user, name='response_user'),
    path('likes/<int:review_id>', views.likes, name='likes'),
    
    path('done.html', views.done, name='done'),
    path('done_contact', views.done_contact, name='done_contact'),
    path('settings_regular', views.settings_regular, name='settings_regular'),
    
    path('submit_review/', views.submit_review, name='submit_review'),
    path('submit_review/review-submitted', views.review_submitted, name='review-submitted'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    #path('edit_response/<int:review_id>/', views.edit_review, name='edit_response'),
    #path('delete_response/<int:review_id>/', views.delete_review, name='delete_response'),
    # overwriting the default template name for reset_password for regular users
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="users/reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_done.html"), name="password_reset_complete"),
   
]
