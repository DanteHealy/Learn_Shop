from django.shortcuts import render, get_object_or_404

from .models import BlogPost, Comment


# Create your views here.

def view_blog(request):
    """ A view to return the index page """
    
    blogpost = BlogPost.objects.all()

    context = {
        'blogpost': blogpost,        
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    """ A view to return the blog post """

    blogpost = get_object_or_404(BlogPost, pk=blog_id)
    comment = blogpost.comment.all()

    context = {
        'blogpost': blogpost,
        'comment': comment,
    }

    return render(request, 'blog/blog_detail.html', context)

