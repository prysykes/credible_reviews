from django.db import models
from django.contrib.auth.models import User
from .import Int_max
from companies.models import Company
from companyusers.models import UserProfileCompany


class UserProfile(models.Model):    
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
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', default='/company_logo/pic.jpg')
    location = models.CharField(max_length=30, choices=state, default=Lagos)
    phone = models.CharField(max_length=30, blank=True, null=True)
    

    def __str__(self):
        return self.user.username

class GenericReview(models.Model):
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
    user_g = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name_g = models.CharField(max_length=250, verbose_name='Name of Company:')
    company_logo_g = models.ImageField(upload_to='generic_logos', default='/company_logo/pic.jpg', verbose_name='Company Logo:')
    picture_evidence_g = models.ImageField(upload_to='evidence', default='/company_logo/pic.jpg', verbose_name='Upload Proof:')
    company_sector_g = models.CharField(max_length=30, choices=sector, default=merchant, verbose_name='Sector')
    company_state_g = models.CharField(max_length=30, choices=state, default=Lagos, verbose_name='State')
    company_address_g = models.TextField(max_length=2000, verbose_name='Company Address:')
    company_website_g = models.CharField(max_length=500, blank=True, null=True, verbose_name='Website:')
    company_email_g = models.EmailField(max_length=500, blank=True, null=True, verbose_name='Company Email:')
    company_phone_g = models.CharField(max_length=500, verbose_name='Company Phone:')
    subject_g = models.CharField(max_length=100, verbose_name='Subject:')
    review_text_g = models.TextField(max_length=500, verbose_name='Your Review:')
    rating_g = Int_max.IntegerRangeField(min_value=1, max_value=5, verbose_name='Your Rating:')
    date_added_g = models.DateField('Review Date', auto_now_add=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.review_text_g


class Review(models.Model):
    # CASCADE ensures that when a company is deleted, their reviews remains
    company = models.ForeignKey(Company, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # SET_NULL ensures that when a user is deleted, their reviews get deleted too
    subject = models.CharField(max_length=100)
    review_text = models.TextField(max_length=500, verbose_name='Your Review:')
    rating = Int_max.IntegerRangeField(min_value=1, max_value=5)
    date_added = models.DateField('Review Date', auto_now_add=True)
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.review_text

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    response = models.TextField(max_length=200, verbose_name='Your Response')
    date_added = models.DateField('Response Date', auto_now_add=True)

    def __str__(self):
        return self.response

class ResponseReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    reply = models.TextField(max_length=200, verbose_name='Your Response')
    date_added = models.DateField('Response Date', auto_now_add=True)

    def __str__(self):
        return self.reply

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)
