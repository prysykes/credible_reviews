from django.shortcuts import render, get_object_or_404

from .models import POST
from django.views.generic import ListView, DetailView

# Create your views here.

class PostListView(ListView):
    queryset = POST.published.all()
    context_object_name = 'posts'
    template_name='blog/blog.html'
    paginate_by = 1
