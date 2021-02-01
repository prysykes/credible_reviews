from .models import *
from django.forms import ModelForm


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)

class CommentReplyForm(ModelForm):

    class Meta:
        model = ReplyComment
        fields = ('reply',)