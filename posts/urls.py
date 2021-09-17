from . import views
from django.conf import settings 
from django.urls import path 

urlpatterns = [     
    path('blog/', views.blog, name='post-list'),
    path('post/<id>/', views.post, name='post-detail'),
]