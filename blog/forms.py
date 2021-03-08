from .models import *
from django.forms import ModelForm, Textarea


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)


class CommentReplyForm(ModelForm):

    class Meta:
        model = ReplyComment
        fields = ('reply',)
        widgets = {
            'reply': Textarea(attrs={'class': 'blog_reply'}),
        }
