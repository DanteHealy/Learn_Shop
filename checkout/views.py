from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J5xbHH8VFj9KK9gotR3G0VdqaXOk5DS13NgvJ28uaVzOZ3JTpRgqvvsoWyILtemcJJuJ2RLIzCy5soaR3wpad7S008rPng4rv',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)