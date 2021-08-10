
from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ A view to render the Cart contents page """

    return render(request, 'cart/cart.html')

# submit Form incl ID and quantity, check if cart variable exists (create if 
#  not), add to cart or update quantity if already there. 

def add_to_cart(request, item_id):
    """ this adds the quantity of the specified product to the Cart"""

    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] +=quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
