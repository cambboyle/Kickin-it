from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

# Product filtering
    if request.GET:

        # Filter by category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Filter by brand
        if 'brand' in request.GET:
            brand = request.GET['brand']
            products = products.filter(brand=brand)

        # Filter by other brands
        if 'other_brands' in request.GET:
            known_brands = ['Nike', 'Adidas', 'New Balance', 'Vans', 'Puma', 'Asics', 'Converse', 'Reebok', 'Hoka One One', 'On Running']
            products = products.exclude(brand__in=known_brands)
            
        # Filter by sale items
        if 'is_sale' in request.GET:
            is_sale = request.GET['is_sale'].lower() == 'true'
            products = products.filter(is_sale=is_sale)

        # Filter by new items
        if 'is_new' in request.GET:
            is_new = request.GET['is_new'].lower() == 'true'
            products = products.filter(is_new=is_new)

        # Filter by gender
        if 'gender' in request.GET:
            gender = request.GET['gender']
            products = products.filter(Q(gender__iexact=gender) | Q(gender__iexact='unisex'))

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
