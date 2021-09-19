from . import views
from django.conf import settings 
from django.urls import path 

urlpatterns = [     
    path('blog/', views.blog, name='post-list'),
    path('post/<id>/', views.post, name='post-detail'),
    path('create/', views.post_create, name='post-create'),
    path('post/<id>/update', views.post_update, name='post-update'),
    path('post/<id>/delete', views.post_delete, name='post-delete'),
    path('search/', views.search, name='search'),
]