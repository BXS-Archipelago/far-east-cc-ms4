from django.shortcuts import render,redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm

from cart.contexts import cart_contents


import stripe

# Create your views here.
def checkout(request):
    # Create payment intent for STRIPE:
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY


    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in the cart at this time. Please contact us for any product advice")
        return redirect(reverse('products'))

    # variables for stripe to gain contents and total from checkout
    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    #set secret key on stripe
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount = stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. It should be in the environment!')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,   
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,     
    }

    return render(request, template, context)
