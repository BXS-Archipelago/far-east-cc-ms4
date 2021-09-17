from . import views
from django.conf import settings 

urlpatterns = [
   
    path('blog/', views.blog, name='blog'),
    path('post/', views.post, name='post'),
]