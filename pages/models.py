from django.db import models

class NewsletterSignUp(models.Model):
    email = models.EmailField(max_length=300)

    def __str__(self):
        return self.email

class Ads(models.Model):
    ad_name = models.CharField(max_length=60, verbose_name='Ad Name' )
    ad_image = models.ImageField(upload_to='advert_images', verbose_name="Ad Image")
    ad_description = models.TextField(max_length=200, verbose_name='Ad Description')
    ad_weight = models.IntegerField(default=0)
    ad_url = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.ad_name
    
