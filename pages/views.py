from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
from django.shortcuts import render, redirect, get_list_or_404
from companies.models import Company
from users.models import Review



def index(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'index.html', context)

def about(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'about.html', context)

""" def submit_review(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('review-submitted')
    context = {
        'form': form
    }
    return render(request, 'submit-review.html', context) """

def browse_review(request):
    reviews = Review.objects.all()
    p = Paginator(reviews, 16)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {
        'reviews': page,
    }
    return render(request, 'browse_review.html', context)

def careers(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'careers.html', context)

def contact(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'contact.html', context)

def cr_seal(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'cr-seal.html', context)

def faq(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'faq.html', context)

def how_to_use(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'how-to-use.html', context)

def login(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'login.html', context)

def online_safety(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'online-safety.html', context)

def privacy_terms(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
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

def company_list(request):
    comps = Company.objects.all()
    context = {
        'comps': comps,
    }

    return render(request, 'company_list.html', context)

def featured_companies(request):
    reviews = Review.objects.all()
    comps = Company.objects.all()
    """
        implementing pagenation for the site
        the 16 their means the number of items per page

        the get('page', 1) tell django to trying gettting the
        page number specified in the querry and if that doesnt work,
        loads page 1 instead.
    """
    p = Paginator(comps, 16)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    
    context = {
        'comps': page,
        'reviews': reviews,
    }
    return render(request, 'featured-companies.html', context)

def review_submitted(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'review-submitted.html', context)
