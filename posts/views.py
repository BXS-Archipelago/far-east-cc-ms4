from django.shortcuts import render

# Create your views here.

def blog(request):
    """
    A view to return the blog page
    """
    return render(request, 'home/blog.html')

def post(request):
    """
    A view to return the blog postings pages
    """
    return render(request, 'home/post.html')
