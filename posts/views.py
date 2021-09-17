from django.shortcuts import render
from .models import Post
# Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

# View to count each time the category name occurred in posts. 
# annotate will return a dictionary where each key is the category to be counted
def get_category_count():
  queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))

  return queryset


def blog(request):
    category_count = get_category_count()
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
      'page_request_var': page_request_var,
      'category_count': category_count,
    }
    return render(request, 'posts/blog.html', context)

def post(request, id):
    """
    A view to return the blog postings pages
    """
    return render(request, 'posts/post.html', {})


