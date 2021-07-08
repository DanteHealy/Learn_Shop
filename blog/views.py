from django.shortcuts import render


# Create your views here.

def view_blog(request):
    """ A view to return the index page """
    
    return render(request, 'blog/blog.html')

