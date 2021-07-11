from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'reason',
        'email',
        'message',
        'responded',
    )


admin.site.register(Contact, ContactAdmin)
