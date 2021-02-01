from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core import serializers


from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import ContactForm

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from companies.models import Company
from users.models import Review, Like
from .forms import NewsletterForm

from django.http import JsonResponse

from django.views.generic.list import ListView

from .filters import CompanyFilter, ReviewFilter

# imports for faster contact us email
from django.core.mail import EmailMessage
from users.views import FasterActivateEmail




def search_business(request):
    if request.method == "GET" and request.GET.get('search_text') != "":
        term = request.GET.get('search_text')
        company = Company.objects.all().filter(company_name__icontains=term, approved=True)
        sector = Company.objects.all().filter(company_sector__icontains=term, approved=True)
        context = {
            'company': company,
            'sector': sector,
        }
        
    return render(request, 'ajax_search.html', context)


def index(request):
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page_range = p.page_range
    
    context = {
        'reviews': page[::-1],
        # used to reverse the out of the paginator list
        'page': page,
        
        'page_range': page_range,
    }

    return render(request, 'index.html', context)

def about(request):
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page_range = p.page_range
    
    context = {
        'reviews': page[::-1],
        # used to reverse the out of the paginator list
        'page': page,
        
        'page_range': page_range,
    }
    return render(request, 'about.html', context)

def browse_review(request, *args, **kwargs):
    likes = Like.objects.all()
    review_list = Review.objects.all()
    if request.is_ajax() and request.method == "GET" and request.GET.get('search_text') != "":
        term = request.GET.get('search_text')
        

        try:
            company = get_object_or_404(Company, company_name__icontains=term, approved=True)
            company_name = {
                'name': company.company_name,
                'id': company.id,
                'not_found': "Company does not exist, please refine search..."
            }
        except:
            company_name = {
                'name': "Company does not exist, please refine search..."
            }

        return JsonResponse(company_name, safe=False)

    filtered_reviews = ReviewFilter(
        request.GET,
        queryset=review_list.order_by('-date_added'),
    )  # instantiate the ReviewFilter class imported at the top of the page with these values
    review_list = filtered_reviews.qs
    paginated_review = Paginator(review_list, 12)
    page_num = int(request.GET.get('page', 1))
    try:
        page = paginated_review.page(page_num)
    except EmptyPage:
        page = paginated_review.page(1)
    context = {
        'filtered_reviews': filtered_reviews, 
        'paginated_review': paginated_review,
        'page': page,
        'likes': likes,

    }   
        
   
    return render(request, 'browse_review.html', context)

def careers(request):
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page_range = p.page_range
    
    context = {
        'reviews': page[::-1],
        # used to reverse the out of the paginator list
        'page': page,
        
        'page_range': page_range,
    }
    return render(request, 'careers.html', context)

def contact(request):
    if request.method == "POST":
        fullname = request.POST['full_name']
        message = request.POST['message']
        receiver = request.POST['receiver']
        subject = request.POST['subject']
        senderplusmessage = f"Fullname: {fullname} \nFrom: {receiver} \n{message}"
        email_subject = subject
        email_body = senderplusmessage
        email = EmailMessage(
                email_subject,
                email_body,
                'noreply@crediblereviews.com',
                [receiver],
                
            )
        FasterActivateEmail(email).start()
        return redirect('done_contact')
    
    
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page_range = p.page_range
    
    context = {
        'reviews': page[::-1],
        # used to reverse the out of the paginator list
        'page': page,
        
        'page_range': page_range,
    }
    return render(request, 'contact.html', context)

def cr_seal(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-date_added')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'cr-seal.html', context)

def faq(request):
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page_range = p.page_range
    
    context = {
        'reviews': page[::-1],
        # used to reverse the out of the paginator list
        'page': page,
        
        'page_range': page_range,
    }
    return render(request, 'faq.html', context)

def how_to_use(request):
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page_range = p.page_range
    
    context = {
        'reviews': page[::-1],
        # used to reverse the out of the paginator list
        'page': page,
        
        'page_range': page_range,
    }
    return render(request, 'how-to-use.html', context)

def login(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-date_added')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'login.html', context)

def online_safety(request):
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page_range = p.page_range
    
    context = {
        'reviews': page[::-1],
        # used to reverse the out of the paginator list
        'page': page,
        
        'page_range': page_range,
    }
    return render(request, 'online-safety.html', context)

def disclaimer(request):
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page_range = p.page_range
    
    context = {
        'reviews': page[::-1],
        # used to reverse the out of the paginator list
        'page': page,
        
        'page_range': page_range,
    }
    return render(request, 'disclaimer.html', context)


def privacy_terms(request):
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page_range = p.page_range
    
    context = {
        'reviews': page[::-1],
        # used to reverse the out of the paginator list
        'page': page,
        
        'page_range': page_range,
    }
    return render(request, 'privacy-terms.html', context)

def display_reviews(request):
    reviews = Review.objects.order_by('?')
    # above code randomizes the returned review objects by the querryset
    context = {
        'reviews': reviews
    }
    return render(request, 'browse_review.html', context)


def validate_business(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'validate-business.html', context)

def filter_result_display(request):
    
    if request.method == "GET":
        term = request.GET.get('term') or ""
    companies_list = Company.objects.all().filter(company_sector__icontains=term)
    filtered_companies = CompanyFilter(
        request.GET,
        queryset=companies_list
    )
    company_list_new = filtered_companies.qs
    paginated_company = Paginator(company_list_new, 9)
    page_num = int(request.GET.get('page', 1))

    try:
        page = paginated_company.page(page_num)
    except EmptyPage:
        page = paginated_company.page(1)
    
    context = {
        'filtered_companies': filtered_companies,
        'paginated_company': paginated_company,
        'page': page,
        'term': term,
    }
    print(term)

    return render(request, 'filter_result_display.html', context)
    
    




def featured_companies(request):
    company_list = Company.objects.all().filter(approved=True)
    filtered_companies = CompanyFilter(
        request.GET,
        queryset=company_list
    )  # instantiate the CompanyFilter class imported at the top of the page with these values
    company_list_new = filtered_companies.qs
    paginated_company = Paginator(company_list_new, 9)
    page_num = int(request.GET.get('page', 1))
    try:
        page = paginated_company.page(page_num)
    except EmptyPage:
        page = paginated_company.page(1)
    context = {
        'filtered_companies': filtered_companies, 
        'paginated_company': paginated_company,
        'page': page,

    } 
    return render(request, 'featured-companies.html', context)


def review_submitted(request):
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page_range = p.page_range
    
    context = {
        'reviews': page[::-1],
        # used to reverse the out of the paginator list
        'page': page,
        
        'page_range': page_range,
    }
    return render(request, 'review-submitted.html', context)

def done_newsletter(request):
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page_range = p.page_range
    
    context = {
        'reviews': page[::-1],
        # used to reverse the out of the paginator list
        'page': page,
        
        'page_range': page_range,
    }
    return render(request, 'done_newsletter.html', context)

