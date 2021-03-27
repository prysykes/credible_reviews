from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('done_newsletter.html', views.done_newsletter, name='done_newsletter'),
    path('browse_review/', views.browse_review, name='browse_review'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
    path('cr-seal/', views.cr_seal, name='cr-seal'),
    path('faq/', views.faq, name='faq'),
    path('how-to-use/', views.how_to_use, name='how-to-use'),
    path('privacy-terms/', views.privacy_terms, name='privacy-terms'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('search_business', views.search_business, name='search_business'),
    path('online-safety/', views.online_safety, name='online-safety'),
    
    #path('submit-review/', views.submit_review, name='submit-review'),
    
    path('validate-business/', views.validate_business, name='validate-business'),
    path('featured-companies/', views.featured_companies, name='featured-companies'),
    path('filter_result_display/term', views.filter_result_display, name='filter_result_display'),
    ]
