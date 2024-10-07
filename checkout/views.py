from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You don't have any items in your bag!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q7HgTRrrhrzfh6oMNuhJXZzeotxceKP4nSXHunKCkwL1Mc3hGC5sK6jEJJNnhkorbe6uRvDmHdwSeJpbXpSgF6T00LTqI1Nfk',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)