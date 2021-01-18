from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import ContactForm

# Create your views here.
from django.shortcuts import render, redirect, get_list_or_404
from companies.models import Company
from users.models import Review
from .forms import NewsletterForm

from django.views.generic.list import ListView

from .filters import CompanyFilter, ReviewFilter



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
    filtered_reviews = ReviewFilter(
        request.GET,
        queryset=Review.objects.all(),
    )
    paginated_reviews = Paginator(filtered_reviews.qs, 12)
    page_num = int(request.GET.get('page', 1))
    try:
        page = paginated_reviews.page(page_num)
    except EmptyPage:
        page = paginated_reviews.page(1)
    context = {
        'filtered_reviews': filtered_reviews,
        'page': page,
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
    if request.method == "POST":
        fullname = request.POST['full_name']
        message = request.POST['message']
        receiver = request.POST['receiver']
        subject = request.POST['subject']
        senderplusmessage = f"Fullname: {fullname} \nFrom: {receiver} \n{message}"
        send_mail(subject, senderplusmessage, settings.EMAIL_HOST_USER, [receiver], fail_silently=False)
        return redirect('done_contact')
    
    
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
    filtered_companies = CompanyFilter(
        request.GET,
        queryset=Company.objects.all()
    )  # instantiate the CompanyFilter class imported at the top of the page with these values
    paginated_companies = Paginator(filtered_companies.qs, 9)
    # .qs above allows a filtered_companies to return a queryset
    """
        implementing pagenation for the site
        the 15 there means the number of items per page

        the get('page', 1) tell django to trying gettting the
        page number specified in the querry and if that doesnt work,
        loads page 1 instead.
    """
    page_num = int(request.GET.get('page', 1))
    try:
        page = paginated_companies.page(page_num)
    except EmptyPage:
        page = paginated_companies.page(1)
    
    """ context = {
        'comps': page,
        'reviews': reviews,
    } """
    context = {
        'filtered_companies': filtered_companies,
        'page': page,

    } 
    return render(request, 'featured-companies.html', context)


def review_submitted(request):
    reviews = Review.objects.all()
    last_twenty = Review.objects.all().order_by('-id')[:20]
    context = {
        'reviews': last_twenty,
    }
    return render(request, 'review-submitted.html', context)

def done_newsletter(request):
    return render(request, 'done_newsletter.html')


