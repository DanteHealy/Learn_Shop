from django import forms
from django.forms import widgets
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Contact form """

    class Meta:
        model = Contact
        fields = [
            'reason',
            'name',
            'email',
            'message',
        ]

