from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from products.models import Product, Review

from checkout.models import Order


@login_required
def profile(request):
    # Show the User's Profile
    profile = get_object_or_404(UserProfile, user=request.user)
    # Post Handler
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure form is valid')
    # move empty form instance into ELSE block so it doesn't wipe form errors:
    else:
        form = UserProfileForm(instance=profile)
    # to render order history in template
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'this is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, template, context)
