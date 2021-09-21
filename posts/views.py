from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, Author
# Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from .forms import CommentForm, PostForm
from django.contrib import messages


# View to count each time the category name occurred in posts. 
# annotate will return a dictionary where each key is the category to be counted
def get_category_count():
  queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))

  return queryset


def blog(request):
    category_count = get_category_count()
    # most_recent will display the latest three items in the right-side column 
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

"""
    A view to return the blog postings pages
    """
def post(request, id):    
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    # post is form.instance.post below
    post = get_object_or_404(Post, id=id)
    # Form for a comment
    form = CommentForm(request.POST or None)
    # This part saves the comment but only passing user and post
    if request.method == "POST":
        if form.is_valid():
          form.instance.user = request.user
          form.instance.post = post
          form.save()
          return redirect(reverse("post-detail", kwargs={
            'id': post.id 
          }))
    context = {
        'post': post,
        'most_recent': most_recent,
        'category_count': category_count,
        'form': form
    }
    return render(request, 'posts/post.html', context)


# To search through blog posts only
def search(request):   
    queryset = Post.objects.all()
    query = request.GET.get('q')    
    if query:
        queryset = queryset.filter(
          # if title contains query OR
          Q(title__icontains=query) |
          # if overview contains query
          Q(overview__icontains=query)
        ).distinct()
        # .distinct will show one result where the term might appear more than once in title and overview together    
  
    context = {
      'queryset': queryset,
    }

    return render(request, 'posts/search_results.html', context)

"""
Functions to update and delete the blog posts by the admin
"""
def post_create(request):
    title = 'Create'
    
    # in attaching author, we need the other parameter request FILES
    form = PostForm(request.POST or None, request.FILES or None)
    # attach author to created posts (see below def get_author)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post-detail', kwargs={
              'id': form.instance.id
            }))
    context = {
        'action': '',
        'title': title,
        'form': form,
        }
    return render(request, "posts/post_create.html", context)
    
# attach author to created posts  
def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

"""
Superuser can edit and update Posts
"""
def post_update(request, id):
    # Get the post to be updated
    title = 'Update'
    print("method", request.method)
    post = get_object_or_404(Post, id=id)
    # the instance being the post itself
    form = PostForm(request.POST or None, request.FILES or None, instance=post)  
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post-detail', kwargs={
              'id': form.instance.id
              }))
            
    # Putting title in context for update
    context = {
      'action': '/update',
      'title': title,
      'form': form,
    }
    return render(request, "posts/post_create.html", context)
 
"""
Superuser can Delete Posts
"""
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("post-list"))




