from django.db import models
# access to user profiles and product data
from profiles.models import UserProfile
from django.contrib.auth.models import User
# for star rating
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# This is so django knows which category each product goes in

class Category(models.Model):
    class Meta: 
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)   

    def __str__(self):
        return self.name


STAR_RATING = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
]


# Model for the Review
class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField(max_length=1300, blank=True)    
    rated = models.PositiveSmallIntegerField(choices=STAR_RATING, null=False)
        
    def __str__(self):
        return self.review

