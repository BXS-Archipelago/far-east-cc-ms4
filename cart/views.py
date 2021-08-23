
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Product
from django.contrib import messages
# Create your views here.


def view_cart(request):
    """ A view to render the Cart contents page """

    return render(request, 'cart/cart.html')

# submit Form incl ID and quantity, check if cart variable exists (create if 
#  not), add to cart or update quantity if already there. 

def add_to_cart(request, item_id):
    """ this adds the quantity of the specified product to the Cart"""
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    

# If item is already in Cart, this sets it equal or increments the number.
#**********************************

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.name} to {cart[item_id]} items. Decisive!')
        
    else:
        cart[item_id] = quantity
        messages.success(request, f'You added {product.name} to the cart. Nice!')
               
    request.session['cart'] = cart
  
    return redirect(redirect_url)

# View to update product quantities or remove the item from Cart

def adjust_cart(request, item_id):
    product = get_object_or_404(Product,pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.name} to {cart[item_id]} items. Decisive!')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your items. If you need any product information, just let us know!')
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

# Remove item from the Shopping Cart
def remove_from_cart(request, item_id):
      
    try:    
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)            
        request.session['cart'] = cart
        messages.success(request, f'Removed {product.name} from your items. If you need any product information, just let us know!')
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)