from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
 
from .models import Product, Category, Review
from django.db.models.functions import Lower

from products.forms import RateForm, ProductForm

from profiles.models import UserProfile


# Create your views here.


def all_products(request):
    """
    A view to show all products including sorting and search queries
    """
    products = Product.objects.all()    
    query = None
    categories = None
    sort = None
    direction = None
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                
        # ***this allows sortkey to sort by name instead of ID ****
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET: 
            # Split into list at commas
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            
    current_sorting = f'{sort}_{direction}'

    # * Use current_categories in context if the user selects multiple or all 
    # categories
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    
    if Product.objects.filter().exists:
        product = get_object_or_404(Product, pk=product_id)
        reviews = Review.objects.filter(product=product)       
        reviews_count = reviews.count()
        running_score = 0
        reviews_avg = 0
        if reviews_count:
            for review in reviews:
                running_score += review.rated
            reviews_avg = running_score / reviews_count
    

    context = {
        'product': product,
        'reviews': reviews,
        'reviews_avg': reviews_avg,
        'reviews_count': reviews_count,
    }

    return render(request, 'products/product_detail.html', context)

@login_required 
def add_product(request):
    # only superuser permission
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the boss can access that!')
        return redirect(reverse('home'))
    # Allow new products to be added to the store

    if request.method == 'POST':
        #post handler for add product view
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'failed to add product. Please ensure the form is valid.')
    else: 
        form = ProductForm()

    template = 'products/add_product.html'
    context = { 
        'form': form
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id): 
    # only superuser permission
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the boss can access that!')
        return redirect(reverse('home'))
    # Allows operator to edit the products
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance = product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully update Product!")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update, Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = { 
        'form': form,
        'product': product,
    }

    return render(request, template, context)

# View for deleting products by site admin
@login_required
def delete_product(request, product_id):
    # only superuser permission
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the boss can access that!')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def rate_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():            
            rate = form.save(commit=False)
            rate.user = user
            rate.product = product            
            rate.save()
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = RateForm()

    template = 'products/rate.html'

    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

