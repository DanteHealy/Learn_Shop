from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

""" A view to return the contact page 
def contact(request):
   
    return render(request, 'contact/contact.html')
"""    

def contact(request):
    """ A view to return the contact page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your message has been successfully sent!'
            )
            return redirect(reverse('contact'))
        else:
            messages.error(
                request,
                'Your message failed to send. \
                Please check the form is valid and try again.'
            )

    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)




""" A view to create a form and send an email 
def post_form(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted 
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_url(post.get_absolute_url)
            subject = f"{cd['name']} sends you a message regarding " \
                    f"{post.reason}"
            
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'contact/contact.html', {'post': post,'form': form, 'sent': sent})
"""
