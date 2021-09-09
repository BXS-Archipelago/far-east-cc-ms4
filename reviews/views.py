# from django.shortcuts import reverse, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# from django.db.models import Avg

# from .models import Review
# from .forms import ReviewForm
# from products.models import Product
# from profiles.models import UserProfile

# @login_required 
# def add_review(request, product_id):
#     """
#     Where a logged-in user can write an independent review:
#     """
#     # Who is the user, what is the product? 
#     user = UserProfile.objects.get(user=request.user)
#     product = get_object_or_404(Product, pk=product_id)
#     # generate our review form
#     review_form = ReviewForm()
#     # The user will submit for these details:
#     review_details = {
#         'title': request.POST['title'],
#         'description': request.POST['description'],
#         'rating': request.POST['rating'],
#     }
#     # How the details will be entered
#     review_form = ReviewForm(review_details)

#     # In progressing the review, avoid duplicate user reviews on same product
#     existing_review = Review.objects.filter(user=user, product=product)
#     # If there is already one review, return message to user.
#     if existing_review.count() > 0:
#         messages.error(request, 'We notice you have already reviewed this item. You can edit your previous one or please contact us with any issues.')

#     # In the instance of no previous reviews, we may progress with it
#     else:
#        # If valid, then the form has been properly populated. 
#         if review_form.is_valid():
#             review = review_form.save(commit=False)
#             review.user = user
#             review.product = product
#             review.save()

#             # send to average rating for a new calculation
#             reviews = review.objects.filter(product=product)
#             avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
#             product.avg_rating = int(avg_rating)
#             product.save()

#             # Success message if added
#             messages.success(request, 'Thanks you for your review')
#         else:
#             # Error message if form was invalid
#             messages.error(request, 'Thank you but please check you filled out the form correctly')

#      return redirect(reverse('product_detail', args=[product.id]))
from django.shortcuts import render, get_object_or_404
from products.models import Product

def rating_view(request): 
    product = get_object_or_404(Product)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)
