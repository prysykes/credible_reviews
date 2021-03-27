from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpFormCompany, UserProfileCompanyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import UserProfileCompany
from pages.models import Ads

from users.models import Review, Response
from users.forms import ResponseForm
from django.urls import reverse

# imports for interuser messages
from . models import Message, ReplyMessage
from . forms import MessageForm, ReplyMessageForm


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pages import filters

from companies.models import Company
from companies.forms import CompanyForm
from django.template.defaultfilters import slugify


# email activation imports
from .utils import company_account_activation_token
from django.core.mail import EmailMessage
from django.views import View
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_text, force_bytes, DjangoUnicodeDecodeError
from django.contrib.sites.shortcuts import get_current_site

# import for faster email
import threading


#from companies.models import Company, Review

from .decorators import unauthenticated_user_company, allowed_users_company

# importing modules to support html email message
from django.http import JsonResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings

# end importing modules to support html email message


class FasterActivateEmailCompany(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    
    def run(self):
        self.email.send(fail_silently=False)


@unauthenticated_user_company
@allowed_users_company(allowed_roles=['company'])
def sign_up_company(request):
    ads = get_list_or_404(Ads, active=True)
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
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, 'Account successfully created for ' + username.upper() +' and activation email sent to: ' + email + ",\n" + " Please visit your email to activate your account...")
            current_user = User.objects.get(username=username)

            #get the useridin64bit
            uidb64 = urlsafe_base64_encode(force_bytes(current_user.pk))
            #not adding .pk will raise type error = get() got multiple values for argument 'uidb64'
            #make a token of the user
            token = company_account_activation_token.make_token(current_user)
            #get the current url
            domain = get_current_site(request).domain
            #second, get link the user would click for activation which takes a view name and kwargs
            link = reverse('company_activation_view', kwargs={'uidb64': uidb64, 'token': token})
            #create activation url the user will see
            activate_url = 'http://'+domain+link

            current_user.is_active = False
            current_user.save()
            email_subject = "Activate Your Account"
            email_body = "Hi "+current_user.username + "Please use this link to activate your acc \n" +activate_url
            email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@crediblereviews.com',
                    [email],
                    
                )
            
            FasterActivateEmailCompany(email).start()
            
            return redirect('user_login')
            
    context = {
        'form': form,
        'ads': ads,
        'profile_form': profile_form
    }
    return render(request, 'companyusers/sign-up-company.html', context)


class CompanyVerificationView(View):
    def get(self, request, uidb64, token):
        print("this is user id", uidb64)
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            print("this is user", user)
            if user.is_active:
                return redirect('user_login')
            else:
                user.is_active = True
                user.save()
                
            messages.success(request, "Account activated successfully")
        except Exception as ex:
            pass
        return redirect('user_login')


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
    return render(request, 'users/user_login.html', context)


def logoutpage_company(request):
    logout(request)
    return redirect('/') #sends the user to homepage after logout

@login_required(login_url='user_login')
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

@login_required(login_url='user_login')
@allowed_users_company(allowed_roles=['company'])
def profile_company(request):
    messages = Message.objects.filter(receiver=request.user)
    replies = ReplyMessage.objects.filter(sender=request.user).order_by('date_sent')
    
    companies = Company.objects.all().filter(approved=True)
    form = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid:
            data = form.save(commit=False)
            data.user = request.user
            company_name = request.POST.get('company_name')
            username = data.user
            data.company_slug = slugify(company_name)
            email_subject = "New Company Listed"
            email_body = f"A new Company have been listed by {username} name is: {company_name}. \n Kindly crosscheck the entry then tick approved or the company delete. "
            email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@crediblereviews.com',
                    ['princealexe2000@gmail.com'],
                    
                )
            
            FasterActivateEmailCompany(email).start()
            
            data.save()
            return redirect('profile_company')
    
    try:
        company = get_object_or_404(Company, user=request.user)
        reviews = company.review_set.all()
        responses = Response.objects.all()
        paginated_reviews = Paginator(reviews, 3)
        page_num = request.GET.get('page', 1)
        company.listed = True
        company.save()


        try:
            page = paginated_reviews.page(page_num)
        except EmptyPage:
            page = paginated_reviews(1)
        context = {
            
            'company': company,
            'companies': companies,
            'reviews': page,
            'page': page,
            'replies': replies,
            #'company_reviews': company_reviews,
            #'total_reviews': total_reviews,
            'responses': responses,
            'info': "No company claimed yet",
            'infor': 'Not Available',
            'form': form,
            'messages': messages,
            'total_messages': len(messages),
        }
    except:
        context = {

            'companies': companies,
            
            'info': "No company claimed yet",
            'infor': 'Not Available',
            'form': form,
        }
        pass

    return render(request, 'companyusers/profile_company.html', context)


@login_required(login_url='user_login')
@allowed_users_company(allowed_roles=['company'])
def reply_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)

    reply_message_form = ReplyMessageForm()
    if request.method == "POST":
         reply_message_form = ReplyMessageForm(request.POST or None)
         if reply_message_form.is_valid:
             data = reply_message_form.save(commit=False)
             data.sender = request.user
             data.message = message
             
             data.save()
             return redirect('profile_company')
    else:
        reply_message_form =  ReplyMessageForm(request.POST or None)
    context = {
       'reply_message_form': reply_message_form, 
    }
    return render(request, 'companyusers/reply_message.html', context)


def request_review_api(request):
    if request.method == 'POST':
        receiver_email = request.POST.get('receiver')
        
        request_review(request, receiver_email)
    
    return redirect('profile_company')


@login_required(login_url='user_login')
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
    FasterActivateEmailCompany(email_msg).start()
    
    
    

def done(request):
    return render(request, 'done.html')




@login_required(login_url='user_login')
@allowed_users_company(allowed_roles=['company'])
def settings_company(request):
    user_profile = request.user.userprofilecompany
    form = UserProfileCompanyForm(instance=user_profile)
    if request.method == "POST":
        form = UserProfileCompanyForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("profile_company")
    context = {
        'form': form,

    }
    return render(request, 'companyusers/settings_company.html', context)
