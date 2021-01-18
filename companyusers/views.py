from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpFormCompany, UserProfileCompanyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import UserProfileCompany
from companies.models import Company
from users.models import Review, Response
from users.forms import ResponseForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pages import filters

#from companies.models import Company, Review

from .decorators import unauthenticated_user_company, allowed_users_company
# importing modules to support html email message
from django.http import JsonResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings

# end importing modules to support html email message



@unauthenticated_user_company
@allowed_users_company(allowed_roles=['company'])
def sign_up_company(request):
    form = SignUpFormCompany()
    profile_form = UserProfileCompanyForm()
    if request.method == 'POST':
        form = SignUpFormCompany(request.POST)
        profile_form = UserProfileCompanyForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            group = Group.objects.get(name='company')
            user.groups.add(group)
                        
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Successfully Created for: ' + user + ",\n" + "Please Log in to continue...")
            return redirect('loginpage_company')
            
    context = {
        'form': form,
        'profile_form': profile_form
    }
    return render(request, 'companyusers/sign-up-company.html', context)


@unauthenticated_user_company
@allowed_users_company(allowed_roles=['company'])
def loginpage_company(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        else:
            messages.info(request, 'Username or Password Incorrect, Try Again...')
            
    context = {

    }
    return render(request, 'companyusers/loginpage_company.html', context)


def logoutpage_company(request):
    logout(request)
    return redirect('/') #sends the user to homepage after logout

@login_required(login_url='loginpage_company')
@allowed_users_company(allowed_roles=['company'])
def response(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    form = ResponseForm()
    if request.method == "POST":
        form = ResponseForm(request.POST or None)
        if form.is_valid:
            data = form.save(commit=False)
            data.user = request.user
            data.review = review
            data.save()
            return redirect('profile_company')
    context = {
        'form': form,
        
        

    }
    
    return render(request, 'companyusers/response.html', context)

@login_required(login_url='loginpage_company')
@allowed_users_company(allowed_roles=['company'])
def profile_company(request):
    
    companies = Company.objects.all()
    try:
        company = get_object_or_404(Company, user=request.user)
        reviews = company.review_set.all()
        responses = Response.objects.all()
        paginated_reviews = Paginator(reviews, 3)
        page_num = request.GET.get('page', 1)

        try:
            page = paginated_reviews.page(page_num)
        except EmptyPage:
            page = paginated_reviews(1)
        context = {

            'companies': companies,
            'reviews': page,
            'page': page,
            #'company_reviews': company_reviews,
            #'total_reviews': total_reviews,
            'responses': responses,
            'info': "No company claimed yet",
            'infor': 'Not Available',
        }
    except:
        context = {

            'companies': companies,
            
            'info': "No company claimed yet",
            'infor': 'Not Available',
        }
        pass

    return render(request, 'companyusers/profile_company.html', context)

def request_review_api(request):
    if request.method == 'POST':
        receiver_email = request.POST.get('receiver')
        
        request_review(request, receiver_email)
    
    return redirect('profile_company')


@login_required(login_url='loginpage_company')
@allowed_users_company(allowed_roles=['company'])
def request_review(request, receiver_email):
    company = get_object_or_404(Company, user=request.user)
    company_id = company.company_slug
    
    html_tpl_path = 'companyusers/request_review.html'
    context_data = {'company': company, 'company_id': company_id,}
    email_html_template = get_template(html_tpl_path).render(context_data)
    receiver_email = receiver_email
        
    email_msg = EmailMessage('Credible Review Request',
                                email_html_template,
                                settings.EMAIL_HOST_USER,
                                [receiver_email],
                                reply_to=['no-reply@crediblereviews.ng'],

                                )  
     
    # this part allows the message to be send as html instead of plain text
    email_msg.content_subtype = 'html'
    email_msg.send(fail_silently=False)
    

def done(request):
    return render(request, 'done.html')




@login_required(login_url='loginpage_company')
@allowed_users_company(allowed_roles=['company'])
def settings_company(request):
    user_profile = request.user.userprofilecompany
    form = UserProfileCompanyForm(instance=user_profile)
    if request.method == "POST":
        form = UserProfileCompanyForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
    context = {
        'form': form,

    }
    return render(request, 'companyusers/settings_company.html', context)
