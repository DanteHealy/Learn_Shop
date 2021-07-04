from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'reason',
        'email',
        'message',
        'responded',
    )


admin.site.register(Contact, ContactAdmin)