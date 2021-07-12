from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """ Comment form """

    class Meta:
        model = Comment
        fields = [
            'comment',
        ]
