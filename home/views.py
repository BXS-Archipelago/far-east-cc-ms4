from django.shortcuts import render
from posts.models import Post

# Create your views here.

def index(request):
    """
    A view to return the index page and blog features
    """
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': featured,
        'latest': latest,
    }

    return render(request, 'home/index.html', context)


