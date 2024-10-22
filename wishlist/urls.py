from django.urls import path
from . import views


urlpatterns = [
    path(
        'add_to_wishlist/<int:product_id>/',
        views.add_to_wishlist,
        name='add_to_wishlist'),
    path(
        'wishlist/',
        views.wishlist,
        name='wishlist'),
    path(
        'remove_from_wishlist/<int:product_id>/',
        views.remove_from_wishlist, 
        name='remove_from_wishlist'),
]
