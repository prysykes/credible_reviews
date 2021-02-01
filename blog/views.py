from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Post, Comment
from django.views.generic import ListView, DetailView

from .forms import CommentForm, CommentReplyForm

# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name='blog/blog.html'
    paginate_by = 3

def post_detail(request, post_slug):
    post = get_object_or_404(Post, post_slug=post_slug)
    comments = post.comments.filter(active=True)
    form_comment = CommentForm()
    

    if request.method == 'POST':
        form_comment = CommentForm(request.POST or None)
        if form_comment.is_valid:
            data = form_comment.save(commit=False)
            data.post = post
            data.name = request.user
            data.email = request.user.email
            print(data.post)
            print(data.name)
            print(data.email)
            data.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            

    

    context = {
        'post': post,
        'form_comment': form_comment,
        'comments': comments,
        
    }

    return render(request, 'blog/post_detail.html', context)

def reply_comment(request):
    pass

   
