from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist

@login_required
def wishlist(request):
    """ A view to return the wishlist page """
    user_profile = UserProfile.objects.get(user=request.user)
    user_wishlist = Wishlist.objects.filter(user_profile=user_profile)

    return render(
        request, 'wishlist/wishlist.html', {'user_wishlist': user_wishlist}
    )

@login_required
def add_to_wishlist(request, product_id):
    """ Add a product to the user's wishlist. """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)

    if Wishlist.objects.filter(user_profile=user_profile, product=product).exists():
        messages.warning(request, f'{product.name} is already in your Wishlist.')
    else:
        wishlist_item = Wishlist.objects.create(user_profile=user_profile, product=product)
        messages.success(request, f'{wishlist_item.product.name} added to Wishlist successfully!')

    return redirect(reverse('product_detail', args=[product_id]))

@login_required
def remove_from_wishlist(request, product_id):
    """ Remove item from Wishlist when remove icon is clicked """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)
    wishlist_item = get_object_or_404(Wishlist, user_profile=user_profile, product=product)
    wishlist_item.delete()
    messages.success(request, f'{product.name} has been successfully removed.')
    return redirect(reverse('wishlist'))