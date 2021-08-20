
from django.shortcuts import render, redirect, reverse, HttpResponse
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
    
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    

# If item is already in Cart, this sets it equal or increments the number.
#**********************************

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    
    else:
        cart[item_id] = quantity
        messages.success(request, f'You added {product.name} to the cart. Nice!')
        
    # why doesn't cart[item_id] become quantity? 
    
    request.session['cart'] = cart
  
    return redirect(redirect_url)

# View to update product quantities or remove the item from Cart

def adjust_cart(request, item_id):
      
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

# Remove item from the Shopping Cart
def remove_from_cart(request, item_id):
      
    try:    
        cart = request.session.get('cart', {})
        cart.pop(item_id)            
        request.session['cart'] = cart

        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)