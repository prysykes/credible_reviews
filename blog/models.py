from django.db import models
from django.contrib.auth.models import User


class POST(models.Model):
    status_choices = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    post_slug = models.SlugField(max_length=255, allow_unicode=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    updated_on = models.DateField(auto_now_add=True)
    created_on = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=status_choices, default='draft')


    class Meta:
        ordering = ('-created_on',)

    
    def __str__(self):
        return self.title
