from django.shortcuts import render, get_object_or_404

from .models import Post


def home(request):
    posts = Post.published.all()
    context = {'posts':posts, }
    return render(request, 'post/index.html', context)


def post_detail(request, slug):
    query = Post.published.all()
    post = get_object_or_404(query, slug=slug)
    context = {'post': post, }
    return render(request, 'post/post.html', context)
