from django.db import models

class NewsletterSignUp(models.Model):
    email = models.EmailField(max_length=300)

    def __str__(self):
        return self.email
