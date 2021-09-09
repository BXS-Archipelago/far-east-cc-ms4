from django.db import models
# access to user profiles and product data
from profiles.models import UserProfile
from products.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator

# For Product reviews model
# class review(models.Model):
#     user = models.ForeignKey(UserProfile, models.CASCADE)
#     product = models.ForeignKey(Product, models.CASCADE)
#     comment = models.TextField(max_length=250)
#     rate = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# For Product ratings model
class Rating(models.Model):    
    user = models.ForeignKey(UserProfile, models.CASCADE)
    score = models.IntegerField(default=0, 
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.name