from django.shortcuts import render, get_object_or_404, redirect
from companies.models import Company
from users.models import Review, Response
from django.contrib.auth.models import User
from django.shortcuts import render
from companies.forms import *
from .forms import ReviewForm


def dynamic_url(request, company_id):
    responses = Response.objects.all()
    company = get_object_or_404(Company, pk=company_id)
    # implementing views count for companies once details page is refreshed or clicked
    company.company_views = company.company_views + 1
    company.save()
    
    companyone_reviews = company.review_set.all()
    total_reviews = len(companyone_reviews)
    form = ReviewForm()
    
    if request.method == "POST":
        form = ReviewForm(request.POST or None)
        if form.is_valid:
            data = form.save(commit=False)
            data.company = company
            print(data.company)
            data.user = request.user
            print(data.user)
            data.save()
            print('saved')
             # to implement average rating
            rating = request.POST.get('rating')
            print(f"This is the rating {rating}")
            companyone = Company.objects.get(pk=company_id)
            print(f"This is the CompanyONe {companyone}")
            companyone.average_rating = round((int(rating) + int(companyone.average_rating))/2)
            companyone.save()
            print(f"This is the Average_rating {companyone.average_rating}")
            return redirect('detail', company_id)
    context = {
        'company': company,
        'companyone_reviews': companyone_reviews,
        'total_reviews': total_reviews,
        'form': form,
        'responses': responses,
        
    }

    return render(request, 'companies/detail.html', context)

""" def review_submitted(request):
    return render(request, 'review-submitted.html')

def submit_review(request):

    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid:
            form.save()
            company = request.POST.get('company')
            print(f"This is the Company {company}")
            rating = request.POST.get('rating')
            print(f"This is the rating {rating}")
            companyone = Company.objects.get(pk=company)
            print(f"This is the CompanyONe {companyone}")
            companyone.average_rating = round((int(rating) + int(companyone.average_rating))/2)
            companyone.save()
            print(f"This is the Average_rating {companyone.average_rating}")
            return redirect('review-submitted')
    context = {
        'form': form
    }
    return render(request, 'submit-review.html', context)

 """