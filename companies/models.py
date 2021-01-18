from django.db import models
from django.contrib.auth.models import User
from . import Int_max

from django.urls import reverse

class Company(models.Model):
    Online_Merchant = 'merch'
    Education = 'edu'
    Transportation = 'trans'
    Hospitalism = 'hosp'
    Healthcare = 'health'
    Construction = 'const'
    Blog = 'blog'
    Finance = 'fin'
    Media = 'media'
    Government_Agency = 'agency'
    Other = 'other'
    Manufacturing = 'manufacturing'
    sector = [
        (Online_Merchant, 'Online Merchant'),
        (Education, 'Education'),
        (Transportation, 'Transportation'),
        (Hospitalism, 'Hospitalism'),
        (Healthcare, 'Healthcare'),
        (Construction, 'Construction'),
        (Blog, 'Blog'),
        (Finance, 'Finance'),
        (Media, 'Media'),
        (Manufacturing, 'Manufacturing'),
        (Government_Agency, 'Government Agency'),
        (Other, 'Other')
    ]
    Free = 'Free'
    Premium = 'Premium'
    package = [
        (Free, 'Free'),
        (Premium, 'Premium')
    ]
    Abuja = 'Abuja'
    Abia = 'Abia'
    Adamawa = 'Adamawa'
    Akwa_Ibom = 'Akwa Ibom'
    Anambra	= 'Anambra'
    Bauchi = 'Bauchi'
    Bayelsa = 'Bayelsa'
    Benue = 'Benue'
    Borno = 'Borno'
    Cross_River	= 'Cross River'
    Delta = 'Delta'
    Ebonyi = 'Ebonyi'
    Edo = 'Edo'
    Ekiti = 'Ekiti'
    Enugu = 'Enugu'
    Gombe = 'Gombe'
    Imo = 'Imo'
    Jigawa = 'Jigawa'
    Kaduna = 'Kaduna'
    Kano = 'Kano'
    Katsina = 'Katsina'
    Kebbi = 'Kebbi'
    Kogi = 'Kogi'
    Kwara = 'Kwara'
    Lagos = 'Lagos'
    Nasarawa = 'Nasarawa'
    Niger = 'Niger'
    Ogun = 'Ogun'
    Ondo = 'Ondo'
    Osun = 'Osun'
    Oyo = 'Ibadan'
    Plateau = 'Plateau'
    Rivers = 'Rivers'
    Sokoto = 'Sokoto'
    Taraba = 'Taraba'
    Yobe = 'Yobe'
    Zamfara = 'Zamfara'

    state = [
        (Abuja, 'Abuja'),
        (Abia, 'Abia'),	
        (Adamawa, 'Adamawa'),	
        (Akwa_Ibom, 'Akwa Ibom'),
        (Anambra, 'Anambra'),
        (Bauchi, 'Bauchi'),
        (Bayelsa, 'Bayelsa'),
        (Benue,	'Benue'),
        (Borno, 'Borno'),
        (Cross_River, 'Cross River'),
        (Delta, 'Delta'),
        (Ebonyi, 'Ebonyi'),
        (Edo, 'Edo'),
        (Ekiti, 'Ekiti'),
        (Enugu, 'Enugu'),
        (Gombe, 'Gombe'),
        (Imo, 'Imo'),
        (Jigawa, 'Jigawa'),
        (Kaduna, 'Kaduna'),
        (Kano, 'Kano'),
        (Katsina, 'Katsina'),
        (Kebbi, 'Kebbi'),
        (Kogi, 'Kogi'),
        (Kwara, 'Kwara'),
        (Lagos, 'Lagos'),
        (Nasarawa, 'Nasarawa'),
        (Niger, 'Niger'),
        (Ogun, 'Ogun'),
        (Ondo, 'Ondo'),
        (Osun, 'Osun'),
        (Oyo, 'Ibadan'),
        (Plateau, 'Plateau'),
        (Rivers, 'Rivers'),
        (Sokoto, 'Sokoto'),
        (Taraba, 'Taraba'),
        (Yobe, 'Yobe'),
        (Zamfara, 'Zamfara')
    ]
    
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Company User')
    company_sector = models.CharField(max_length=30, choices=sector, default=Online_Merchant, verbose_name='Sector')
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    company_logo = models.ImageField(upload_to='company_logos', blank=True, null=True)
    company_state = models.CharField(max_length=30, choices=state, default=Lagos, verbose_name='State')
    company_address = models.TextField(max_length=2000)
    average_rating = Int_max.IntegerRangeField(default=0, verbose_name='Avg', min_value=1, max_value=5)
    total_views = models.IntegerField(default=0)
    company_website = models.CharField(max_length=500, blank=True, null=True)
    company_email = models.EmailField(max_length=500, blank=True, null=True)
    company_phone = models.CharField(max_length=500)
    package_chosen = models.CharField(max_length=8, choices=package, default=Free)
    company_views = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    advert = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse("detail", kwargs={ "id": self.id })
    
    def __str__(self):
        return self.company_name
    
    def __repr__(self):
        return self.company_name
    
    
    
    
    


""" class Review(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL) 
    # SET_NULL ensures that when a company is deleted, their reviews remains
    reviewers_name = models.CharField(max_length=250, verbose_name='Reviewed By: (Your Name)')
    review_text = models.TextField(max_length=500, verbose_name='Your Review: (Maximum of 200 Words)')
    rating = Int_max.IntegerRangeField(min_value=1, max_value=5)
    date_added = models.DateField('Review Date', auto_now_add=True)

    def __str__(self):
        return self.review_text + self.reviewers_name """

