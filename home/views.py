from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    ''' View for the home page '''

    featured_products = Product.objects.filter(is_featured=True).order_by('?')[:8]

    return render(request, 'home/index.html', {'products': featured_products})