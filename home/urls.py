from django.urls import path 
from . import views
from django.conf import settings 


urlpatterns = [
    path('', views.index, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
]