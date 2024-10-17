from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wishlist


@login_required
def add_to_wishlist(request, product_name):
    """ A view to add an item to the user's wishlist """
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user, 
        product_name=product_name
    )
    if created:
        messages.success(request, f"{product_name} added to your wishlist.")
    else:
        messages.info(request, f"{product_name} is already in your wishlist.")
    return redirect('view_wishlist')


@login_required
def view_wishlist(request):
    """ A view to show the user's wishlist """
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist/view_wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def remove_from_wishlist(request, product_name):
    """ A view to remove an item from the user's wishlist """
    wishlist_item = get_object_or_404(Wishlist, user=request.user, product_name=product_name)
    wishlist_item.delete()
    messages.success(request, f"{product_name} removed from your wishlist.")
    return redirect('view_wishlist')
