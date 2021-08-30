from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    # each user has one profile, and one profile to one user only.
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    # This is the client's source for address and delivery information as well as order history
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label="Country *", null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    # string method to return user name
    def __str__(self):
        return self.user.username

# Each time a user object is saved, it will create either profile or save to # the profile as an update.
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
   # if its a newly created profile...
    if created:
        UserProfile.objects.create(user=instance)
    # alternatively, if existing just save the profile again in case of update.
    instance.userprofile.save()
