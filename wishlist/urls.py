from django.urls import path
from . import views

urlpatterns = [
    path('add/<str:product_name>/', views.add_to_wishlist, name='add_wishlist'),
    path('view/', views.view_wishlist, name='view_wishlist'),
    path('remove/<str:product_name>/', views.remove_from_wishlist, name='remove_wishlist'),
]
