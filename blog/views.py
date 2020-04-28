from django.shortcuts import render, get_object_or_404
from .models import Blog_post

def blog_home(request):
    posts = Blog_post.objects.order_by("-date")[:10]
    dropdownPosts = Blog_post.objects.order_by("-date")[:5]
    return render(request, "blog/blog_home.html", {"posts": posts, "dropdownPosts": dropdownPosts})

def blog_archive(request):
    posts = Blog_post.objects.order_by("-date")
    dropdownPosts = Blog_post.objects.order_by("-date")[:5]
    return render(request, "blog/blog_archive.html", {"posts": posts, "dropdownPosts": dropdownPosts})

def post(request, post_id):
    post = get_object_or_404(Blog_post, pk=post_id)
    dropdownPosts = Blog_post.objects.order_by("-date")[:5]
    return render(request, "blog/post.html", {"post": post, "dropdownPosts": dropdownPosts})