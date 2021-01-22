from django.db import models
from django.contrib.auth.models import User
from . import Int_max

from django.urls import reverse

from django.contrib.postgres.fields import ArrayField

class Company(models.Model):
    merchant = 'online merchant'
    forex = 'forex company'
    betting = 'sports betting'
    fooddrug = 'food and drug'
    education = 'education'
    transportation = 'transportation'
    logistics = 'logistics'
    hospitality = 'hospitality'
    healthcare = 'health'
    construction = 'construction'
    handle = 'social media handle'
    blog = 'blog'
    finance = 'finance'
    media = 'media'
    agency = 'governement agency'
    other = 'other'
    manufacturing = 'manufacturing'
    sector = [
        (merchant, 'Online Merchant'),
        (forex, 'Forex Company'),
        (betting, 'Sports Betting'),
        (fooddrug, 'Food and Drug'),
        (education, 'Education'),
        (transportation, 'Transportation'),
        (logistics, 'Logistics'),
        (hospitality, 'Hospitality'),
        (healthcare, 'Healthcare'),
        (construction, 'Construction'),
        (blog, 'Blog'),
        (handle, 'Social Media Handle'),
        (finance, 'Finance'),
        (media, 'Media'),
        (manufacturing, 'Manufacturing'),
        (agency, 'Governement Agency'),
        (other, 'Other')
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
    company_sector = models.CharField(max_length=30, choices=sector, default=merchant, verbose_name='Sector')
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    company_logo = models.ImageField(upload_to='company_logos', blank=True, null=True, verbose_name='Company Logo')
    sample_pics_one = models.ImageField(upload_to='sample_pics', blank=True, null=True, verbose_name='Upload Company Picture')
    sample_pics_two = models.ImageField(upload_to='sample_pics', blank=True, null=True, verbose_name='Upload Company Picture')
    sample_pics_three = models.ImageField(upload_to='sample_pics', blank=True, null=True, verbose_name='Upload Company Picture')
    sample_pics_four = models.ImageField(upload_to='sample_pics', blank=True, null=True, verbose_name='Upload Company Picture')
    
    company_state = models.CharField(max_length=30, choices=state, default=Lagos, verbose_name='State')
    company_address = models.TextField(max_length=2000)
    rating_array = ArrayField(models.IntegerField(), size=50, default=list)
    average_rating = Int_max.IntegerRangeField(default=1, verbose_name='Avg', min_value=1, max_value=5)
    total_views = models.IntegerField(default=0)
    company_website = models.CharField(max_length=500, blank=True, null=True)
    company_email = models.EmailField(max_length=500, blank=True, null=True)
    company_phone = models.CharField(max_length=500)
    package_chosen = models.CharField(max_length=8, choices=package, default=Free)
    company_views = models.IntegerField(default=0)
    listed = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    advert = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)

    company_slug = models.SlugField(max_length=255, allow_unicode=True)# used to get company name in url instead of ID

    def get_absolute_url(self):# used to get company name in url instead of ID
        """Returns the url to access a particular instance of the model."""
        return reverse("detail", kwargs={ "slug": self.slug })
    
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

