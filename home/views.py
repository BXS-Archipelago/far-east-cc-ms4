from django.shortcuts import render
from posts.models import Post

# Create your views here.

def index(request):
    """
    A view to return the index page and blog features
    """
    queryset = Post.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }

    return render(request, 'home/index.html', context)


