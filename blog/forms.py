from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """ Contact form """

    class Meta:
        model = Comment
        fields = [
            'user',
            'comment',
        ]
