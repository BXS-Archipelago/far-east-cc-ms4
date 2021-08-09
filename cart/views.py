
from django.shortcuts import render

# Create your views here.


def view_cart(request):
    """ A view to render the Cart contents page """

    return render(request, 'cart/cart.html')