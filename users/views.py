from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpFormRegular, UserProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import UserProfile, Review, Response




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
            user = form.save()
            group = Group.objects.get(name='regular')
            user.groups.add(group)
            """
             commit=False prevents the profile form from being saved in the database
             this enable use to associate it with the user model prior to submission
            """
            profile = profile_form.save(commit=False)
            profile.user = user  # oneToOne relationship comes into play here
            profile.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Successfully Created for: ' + user.upper() + ",\n" + "Please Log in to continue...")
            return redirect('loginpage_regular')

    context = {
        'form': form,
        'profile_form': profile_form
    }
    return render(request, 'users/sign-up.html', context)


@unauthenticated_user_regular
@allowed_users_regular(allowed_roles=['regular'])
def loginpage_regular(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('profile_regular')
        else:
            messages.info(request, 'Username or Password Incorrect, Try Again...')
            
    context = {

    }
    return render(request, 'users/loginpage_regular.html', context)



def logoutpage_regular(request):
    logout(request)
    return redirect('/')
    

@login_required(login_url='loginpage_company')
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

@login_required(login_url='loginpage_regular')
@allowed_users_regular(allowed_roles=['regular'])
def profile_regular(request):
    # would contain all companies reviewed by the user
    companies = []
    responses = Response.objects.all()
    reviews = Review.objects.filter(user=request.user)
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
        'reviews': reviews,
        'total_reviews': total_reviews,
        'responses': responses,
        'total_companies': total_companies,
        'companies': companies,
        

    }
    return render(request, 'users/profile_regular.html', context)

def review_submitted(request):
    return render(request, 'users/review-submitted.html')

@login_required(login_url='loginpage_regular')
@allowed_users_regular(allowed_roles=['regular'])
def submit_review(request):
    form = ReviewForm()
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
            print(f"This is the user {data.user}")
            
            data.save()
            print('Saved')
            # to implement average rating
            company = request.POST.get('company')
            print(f"This is the submitted Company {company}")
            rating = request.POST.get('rating')
            print(f"This is the rating {rating}")
            companyone = Company.objects.get(pk=company)
            print(f"This is the CompanyONe {companyone}")
            companyone.average_rating = round((int(rating) + int(companyone.average_rating))/2)
            companyone.save()
            print(f"This is the Average_rating {companyone.average_rating}")
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

def done(request):
    return render(request, 'done.html')

def done_contact(request):
    return render(request, 'done_contact.html')
    
@login_required(login_url='loginpage_regular')
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

