from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction= None
    current_gender = None

    # Product filtering
    if request.GET:

        # Sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'brand':
                sortkey = 'lower_brand'
                products = products.annotate(lower_brand=Lower('brand'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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
            current_gender = gender
            products = products.filter(Q(gender__iexact=gender) | Q(gender__iexact='unisex'))

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_gender': current_gender,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ A view to add a new product """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to add products.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product =form.save()
            messages.success(request, 'Product added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please double check your information.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ A view to edit an existing product """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to add products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to update product. \
                Please double check the form.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Editing product: {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ A view to delete an existing product """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to add products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Product "{product.name}" deleted!')
    return redirect(reverse('products'))
