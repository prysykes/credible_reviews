from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpFormRegular, UserProfileForm
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Review, Response, Like
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

#begin imports for reset email
from django.core.mail import EmailMessage
from django.views import View
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.contrib.sites.shortcuts import get_current_site
from .utils import account_activation_token


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pages import filters



from companies.models import Company
from users.forms import ReviewForm, ResponseForm
from .decorators import unauthenticated_user_regular, allowed_users_regular

@unauthenticated_user_regular
@allowed_users_regular(allowed_roles=['regular'])
def sign_up(request):
    form = SignUpFormRegular()
    profile_form = UserProfileForm()
    if request.method == "POST":
        form = SignUpFormRegular(request.POST)
        # request.FILES because we are working with an image field
        profile_form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            
              # uses this to set the user as inactive to enable send actiation email
            user = form.save()
            
            
            
            """
             commit=False prevents the profile form from being saved in the database
             this enable use to associate it with the user model prior to submission
            """
            profile = profile_form.save(commit=False)
            profile.user = user  # oneToOne relationship comes into play here
            profile.save()
            group = Group.objects.get(name='regular')
            user.groups.add(group)
            
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, 'Account successfully created for ' + username.upper() +' and activation email sent to: ' + email + ",\n" + " Please visit your email to activate your account...")
            current_user = User.objects.get(username=username)

            #implementing activate acc
            uidb64 = urlsafe_base64_encode(force_bytes(current_user.pk))
            #without forcebytes, encoded url cant be sent through the network
            token = account_activation_token.make_token(current_user)
            #for this, utils.py was created
            # first we get the current site url thus
            domain = get_current_site(request).domain
            #second, get link the user would click for activation which takes a view name and kwargs
            link = reverse('activate_account', kwargs={'uidb64':uidb64, 'token':token})
            #activate_account above has already been created in the app urls.py path
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
            email.send(fail_silently=False)
            
            return redirect('user_login')

    context = {
        'form': form,
        'profile_form': profile_form
    }
    return render(request, 'users/sign-up.html', context)


#this class is called once the email activate link is clicked
class verification_view(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))  #get the user Id sent with the request
            user = User.objects.get(pk=id)
            print("this is ", user)

            # if not account_activation_token.check_token(user, token):
            #     return redirect('user_login')


            if user.is_active:
                return redirect('user_login')
            else:
                user.is_active = True
                user.save()

            messages.success(request, "Account activated successfully")
        except Exception as ex:
            pass
        
        return redirect('user_login')
    

@unauthenticated_user_regular
@allowed_users_regular(allowed_roles=['regular', 'company'])
def user_login(request):
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page_range = p.page_range
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.user.groups.filter(name='regular').exists():
                    return redirect('profile_regular')
                elif request.user.groups.filter(name='company').exists():
                    return redirect('profile_company')
            else:
                messages.info(request, 'Your account is not yet activated...')
        
        else:
            messages.info(request, 'Username or Password Incorrect, Try Again...')
            
    context = {
        'reviews': page[::-1],
        # used to reverse the out of the paginator list
        'page': page,
        
        'page_range': page_range,
    }
    return render(request, 'users/user_login.html', context)



def logoutpage_regular(request):
    logout(request)
    return redirect('/')
    

@login_required(login_url='user_login')
@allowed_users_regular(allowed_roles=['regular'])
def response_user(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    form = ResponseForm()
    if request.method == "POST":
        form = ResponseForm(request.POST or None)
        if form.is_valid:
            data = form.save(commit=False)
            data.user = request.user
            data.review = review
            data.save()
            return redirect('profile_regular')
    context = {
        'form': form,
        
        

    }
    
    return render(request, 'users/response_user.html', context)

@login_required(login_url='user_login')
@allowed_users_regular(allowed_roles=['regular'])
def profile_regular(request):
    # would contain all companies reviewed by the user
    responses = Response.objects.all()
    reviews = Review.objects.filter(user=request.user)
    companies = []
    paginated_reviews = Paginator(reviews, 3)
    page_num = int(request.GET.get('page', 1))

    try:
        page = paginated_reviews.page(page_num)
    except EmptyPage:
        page = paginated_reviews.page(1)
    
 
    """
    Loops through the reviews where user is the logged in user
    then accesses the companies associated with the reviews
    and automatically add it to the companies list above.
    """
    for review in reviews:
        company = review.company
        if company not in companies:
            companies.append(company)
    total_companies = len(companies)
    total_reviews = len(reviews)
    
    
    context = {
        'reviews': page,
        'total_reviews': total_reviews,
        'responses': responses,
        'total_companies': total_companies,
        'companies': companies,
        'page': page,
        

    }
    return render(request, 'users/profile_regular.html', context)

def review_submitted(request):
    return render(request, 'users/review-submitted.html')

@login_required(login_url='user_login')
@allowed_users_regular(allowed_roles=['regular'])
def submit_review(request):
    form = ReviewForm()
    if request.is_ajax():
        
        term = request.GET.get('term')
        companies = Company.objects.all().filter(company_name__icontains=term)
        response_content = list(companies.values())
        
        return JsonResponse(response_content, safe=False)

    if request.method == 'POST':
        form = ReviewForm(request.POST or None)
        if form.is_valid:
            data = form.save(commit=False)
            """
                to implement the average rating feature, first get the particular company from the company
                chosen by the reviewer/ Use this company as a primary key to get that particular company from
                the database. Then use the gotten company to access the company objects like the average rating field.
            """
            """
                The reason for commit=False is allow us assign request.user to the user field in the 
                submitted form. So we can be able to access it in Template.
            """
            data.user = request.user
            
            
            data.save()
            
            # to implement average rating
            company = request.POST.get('company')
            
            rating = request.POST.get('rating')
            
            companyone = Company.objects.get(pk=company)
           
            companyone.average_rating = round((int(rating) + int(companyone.average_rating))/2)
            companyone.save()
            
            return redirect('profile_regular')
    context = {
        'form': form,
                
    }
    return render(request, 'users/submit-review.html', context)

def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST or None, instance=review)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('profile_regular')
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
    }
    return render(request, 'users/submit-review.html', context)

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect('profile_regular')

def edit_response(request, response_id):
    response = get_object_or_404(Response, pk=response_id)
    if request.method == "POST":
        form = ResponseForm(request.POST or None, instance=response)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('profile_regular')
    else:
        form = ResponseForm(instance=response)
    context = {
        'form': form,
    }
    return render(request, 'users/submit-review.html', context)

def delete_response(request, response_id):
    response = get_object_or_404(Response, pk=response_id)
    response.delete()
    return redirect('profile_regular')

def done(request):
    return render(request, 'done.html')

def done_contact(request):
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
    return render(request, 'done_contact.html', context)
    
@login_required(login_url='user_login')
@allowed_users_regular(allowed_roles=['regular'])
def settings_regular(request):
    user_profile = request.user.userprofile
    form = UserProfileForm(instance=user_profile)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():            
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'users/settings_regular.html', context)

@login_required(login_url='user_login')
@allowed_users_regular(allowed_roles=['regular'])
def likes(request, review_id):
    review_to_like = get_object_or_404(Review, id=review_id)
    
    try:
        if get_object_or_404(Like, review=review_to_like, user=request.user):
            messages.error(request, "You can't like a review more than once!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
    except:
        user_like = request.user
        like = Like() #instantiates a like
        like.review = review_to_like # accesses a like attribute
        like.user = user_like # accesses a like attribute
        like.like_count +=1 # adds one to the like count
        like.save() # saves the like

    
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    #returns user to same page after liking the review, helps in implementing logic on any page
