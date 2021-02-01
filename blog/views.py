from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Post, Comment
from django.views.generic import ListView, DetailView

from .forms import CommentForm

# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name='blog/blog.html'
    paginate_by = 3

def post_detail(request, post_slug):
    post = get_object_or_404(Post, post_slug=post_slug)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    

    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid:
            data = form.save(commit=False)
            data.post = post
            print(data.post)
            data.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            

    

    context = {
        'post': post,
        'form': form,
        'comments': comments,
        
    }

    return render(request, 'blog/post_detail.html', context)

   
