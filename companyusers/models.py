from django.db import models
from django.contrib.auth.models import User


class UserProfileCompany(models.Model):
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

    Free = 'Free'
    Premium = 'Premium'
    package = [
        (Free, 'Free'),
        (Premium, 'Premium')
    ]

    
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)    
    designation = models.CharField(max_length=20)
    package = models.CharField(max_length=30, choices=package, default=Free, verbose_name="Choose a Package")
    profile_photo = models.ImageField(upload_to='rep_picture', default='pic.jpg', blank=True, null=True)
    location = models.CharField(max_length=30, choices=state, default=Lagos)
    phone = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(max_length=500, verbose_name='Company Address', blank=True, null=True)
    claimed = models.BooleanField(default=False)
  
    def __str__(self):
        return str(self.user)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender", verbose_name="Sender's Name")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver", verbose_name="Receiver's Name")
    subject = models.CharField(max_length=100, verbose_name="Subject")
    message = models.TextField(max_length=500, verbose_name="Message")
    date_sent = models.DateTimeField('message date', auto_now_add=True)

    def __str__(self):
        return self.subject

class ReplyMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reply_sender", verbose_name="Sender's Name")
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    reply = models.TextField(max_length=500, verbose_name="Reply")
    date_sent = models.DateTimeField('message date', auto_now_add=True)

    def __str__(self):
        return self.reply

    




