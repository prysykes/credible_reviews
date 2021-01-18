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
    profile_picture = models.ImageField(upload_to='profile_pics', default='pic.jpg')
    location = models.CharField(max_length=30, choices=state, default=Lagos)
    phone = models.CharField(max_length=30, blank=True, null=True)
    

    def __str__(self):
        return self.user.username


class Review(models.Model):
    # CASCADE ensures that when a company is deleted, their reviews remains
    company = models.ForeignKey(Company, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # SET_NULL ensures that when a user is deleted, their reviews get deleted too
    review_text = models.TextField(max_length=500, verbose_name='Your Review: (Maximum of 200 Words)')
    rating = Int_max.IntegerRangeField(min_value=1, max_value=5)
    helpful = models.IntegerField(default=0)
    date_added = models.DateField('Review Date', auto_now_add=True)

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

