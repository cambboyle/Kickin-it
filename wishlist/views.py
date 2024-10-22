from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

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
    """A view to add an item to the wishlist"""
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)

    if Wishlist.objects.filter(
            user_profile=user_profile, product=product).exists():
        messages.warning(
            request, f'{product.name} is already in your Wishlist.')
    else:
        Wishlist.objects.create(
            user_profile=user_profile, product=product)
        messages.success(
            request, f'{product.name} added to Wishlist successfully!')

    # Redirect back to the product detail page or another suitable page
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_from_wishlist(request, product_id):
    """ A view to remove an item from the wishlist """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)
    wishlist_item = Wishlist.objects.filter(
        user_profile=user_profile, product=product).first()

    if wishlist_item:
        wishlist_item.delete()
        messages.success(
            request, f'{product.name} has been successfully removed.')
    else:
        messages.warning(
            request, f'{product.name} was not found in your Wishlist.')

    return redirect(reverse('wishlist'))
