from django.shortcuts import render,redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in the cart at this time. Please contact us for any product advice")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,   
        'stripe_public_key': 'pk_test_51J7ycGG7TwB0JNQzuQuCr0dhot9q2wTtzX1tMVcT61If1IulQWC4vJp1zd8bxalcS9iIelaI1klt1jXj4IUD1cQN00cQu3JnXS',
        'client_secret': 'test client secret',     
    }

    return render(request, template, context)
