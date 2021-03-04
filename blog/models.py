from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    """ An object manager to get only blog posts that have already been published"""
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
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
    tags = TaggableManager()


    class Meta:
        ordering = ('-created_on',)
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.post_slug])
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments')
    email = models.EmailField()
    content = models.TextField(verbose_name='Your Comment')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return f"Comment by {self.name} on {self.post}"

class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment')
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_replycomment')
    email = models.EmailField()
    reply = models.TextField(verbose_name='Reply')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.reply

    
