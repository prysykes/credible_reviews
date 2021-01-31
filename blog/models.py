from django.db import models
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    """ An object manager to get only blog posts that have already been published"""
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class POST(models.Model):
    status_choices = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    post_slug = models.SlugField(max_length=255, allow_unicode=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    post_image = models.ImageField(upload_to="blog_images", null=True, blank=True)
    content = models.TextField()
    updated_on = models.DateField(auto_now_add=True)
    created_on = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=status_choices, default='draft')
    featured = models.BooleanField(default=False)
    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering = ('-created_on',)

    
    def __str__(self):
        return self.title
