from django.shortcuts import render
from .models import Post
# Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog(request):
  # most_recent will display the latest three items in the right side of page
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all()
    # render the pagination 
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
      paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
      paginated_queryset = paginator.page(1)
    except EmptyPage:
      paginated_queryset = paginator.page(paginator.num_pages)

    context = {
      'most_recent': most_recent,
      'queryset': paginated_queryset,
      'page_request_var': page_request_var
    }
    return render(request, 'posts/blog.html', context)

def post(request):
    """
    A view to return the blog postings pages
    """
    return render(request, 'posts/post.html')


