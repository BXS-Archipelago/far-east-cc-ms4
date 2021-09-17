from django.shortcuts import render

# Create your views here.

def post(request):
    """
    A view to return the blog postings pages
    """
    return render(request, 'home/post.html')
