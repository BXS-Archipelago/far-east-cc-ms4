from django.contrib import admin
from .forms import PostForm
from .models import Author, Category, Post, Comment

class PostAdmin(admin.ModelAdmin):
    form = PostForm

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

