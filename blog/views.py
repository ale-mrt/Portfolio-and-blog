from django.shortcuts import render, get_object_or_404
from .models import Blog_post

# view di blog

# view della home. restituisce la pagina con gli utlimi dieci post per la visualizzazione nella pagina e gli ultimi cinque per il bottone di dropdwon
def blog_home(request):
    posts = Blog_post.objects.order_by("-date")[:10]
    dropdownPosts = Blog_post.objects.order_by("-date")[:5]
    return render(request, "blog/blog_home.html", {"posts": posts, "dropdownPosts": dropdownPosts})

# view dell'archivio. restituisce la pagina con tutti i post post per la visualizzazione nella pagina e gli ultimi cinque per il bottone di dropdwon
def blog_archive(request):
    posts = Blog_post.objects.order_by("-date")
    dropdownPosts = Blog_post.objects.order_by("-date")[:5]
    return render(request, "blog/blog_archive.html", {"posts": posts, "dropdownPosts": dropdownPosts})

# view del post singolo. restituisce gli ultimi cinque post per il bottone di dropdwon e il post ottenuto col suo id
def post(request, post_id):
    post = get_object_or_404(Blog_post, pk=post_id)
    dropdownPosts = Blog_post.objects.order_by("-date")[:5]
    return render(request, "blog/post.html", {"post": post, "dropdownPosts": dropdownPosts})