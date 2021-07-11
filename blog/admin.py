from django.contrib import admin
from .models import BlogPost, Comment


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'body_text',
        'created',
        'updated',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'post',
        'created_at',
        'comment',
    )


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
