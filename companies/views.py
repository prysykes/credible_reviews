from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from companies.models import Company
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from users.models import Review, Response
from django.contrib.auth.models import User
from django.shortcuts import render
from companies.forms import *
from .forms import ReviewForm
from users.models import Like
from pages.filters import ReviewFilter


def dynamic_url(request, *args, **kwargs):
    likes = Like.objects.all()
    responses = Response.objects.all()
    company = Company.objects.get(company_slug=kwargs.get('company_id'))
    # used to return the name of the company instead of digits on detail page
    
    avg_rating = company.rating_array

    """ implementing views count for companies
     once details page is refreshed or clicked
    """
    company.company_views = company.company_views + 1
    company.save()
    # end of views count

    # get all reviews under a particular company fetched with company_id
    companyone_reviews = company.review_set.all()
    filtered_companyone_reviews = ReviewFilter(
        request.GET,
        queryset=companyone_reviews.order_by('-date_added'),
    )
    companyone_reviews = filtered_companyone_reviews.qs
    paginated_companyone_reviews = Paginator(companyone_reviews, 6)
    page_num = int(request.GET.get('page', 1))
    try:
        page = paginated_companyone_reviews.page(page_num)
    except EmptyPage:
        page = paginated_companyone_reviews.page(1)
    total_reviews = len(companyone_reviews)
    form = ReviewForm()
    
    if request.method == "POST":
        form = ReviewForm(request.POST or None)
        if form.is_valid:
            data = form.save(commit=False)
            data.company = company
            data.user = request.user
            data.save()
             # to implement average rating
            rating = request.POST.get('rating')
            companyone = company
            companyone.rating_array.append(int(rating))
            new_rating = (sum(companyone.rating_array)/len(companyone.rating_array))
            
            if 4.5 <= new_rating <= 5:
                companyone.average_rating = 5
            elif 4.0 <= new_rating < 4.5:
                companyone.average_rating = 4
            elif 3.0 <= new_rating < 4.0:
                companyone.average_rating = 3
            elif 2.0 <= new_rating < 3:
                companyone.average_rating = 2
            elif 1.0 <= new_rating < 2:
                companyone.average_rating = 1
            
            companyone.save()
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            # comes back to the current page
    context = {
        'company': company,
        'companyone_reviews': page[::-1],
        'page': page,
        'filtered_companyone_reviews': filtered_companyone_reviews,
        'total_reviews': total_reviews,
        'form': form,
        'responses': responses,
        'likes': likes,
        
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