from django import forms
from django.forms import widgets
from .models import Comment


class CommentForm(forms.ModelForm):
    """ Comment form """

    class Meta:
        model = Comment
        fields = [
            'comment',
        ]
