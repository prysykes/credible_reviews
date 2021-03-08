from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Post, Comment, ReplyComment
from django.views.generic import ListView, DetailView

from .forms import CommentForm, CommentReplyForm

from taggit.models import Tag
from django.db.models import Count

from django.contrib.auth.decorators import login_required

from users.decorators import allowed_users_regular, unauthenticated_user_regular

# Create your views here.

def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    paginated_posts = Paginator(object_list, 3)
    page_num = request.GET.get('page')

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = object_list.filter(tags__in=[tag])
        paginated_posts = Paginator(posts, 1)
        page_num = request.GET.get('page')
        try:
            posts = paginated_posts.page(page_num)
        except PageNotAnInteger:
            posts = paginated_posts.page(1)
        except EmptyPage:
            posts = paginated_posts.page(1)
    else:
        
        try:
            posts = paginated_posts.page(page_num)
        except PageNotAnInteger:
            posts = paginated_posts.page(1)
        except EmptyPage:
            posts = paginated_posts.page(1)
    
   
    context = {
        'posts': posts,
        'paginated_posts': paginated_posts,
        'tag': tag,
    }

    return render(request, 'blog/blog.html', context)

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name='blog/blog.html'
    paginate_by = 3

def post_detail(request, *args, **kwargs):
    post = get_object_or_404(Post, post_slug=kwargs.get('post_slug'))
    comments = post.comments.filter(active=True)
    replies = ReplyComment.objects.all()
    post_tag_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tag_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags')[:4]
    form_reply = CommentReplyForm()
    form_comment = CommentForm()

    if request.method == 'POST':
        form_comment = CommentForm(request.POST or None)
        if form_comment.is_valid:
            data = form_comment.save(commit=False)
            data.post = post
            data.name = request.user
            data.email = request.user.email
            data.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    context = {
        'post': post,
        'form_comment': form_comment,
        'comments': comments,
        'similar_posts': similar_posts,
        'form_reply': form_reply,
        'replies': replies,
        
    }

    return render(request, 'blog/post_detail.html', context)

@login_required(login_url='user_login')
def reply_comment(request, post_slug, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    form_reply = CommentReplyForm()
    if request.method == 'POST':
        form_reply = CommentReplyForm(request.POST or None)
        if form_reply.is_valid:
            data = form_reply.save(commit=False)
            data.comment = comment
            data.name = request.user
            data.email = request.user.email
            data.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='user_login')
def delete_reply(request, reply_id):
    reply = get_object_or_404(ReplyComment, pk=reply_id)
    reply.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
