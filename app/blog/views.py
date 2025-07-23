from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def post_list(request):
    object_list = Post.objects.filter(status='published')
    paginator = Paginator(object_list, 3)  # 3 posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def category_view(request, category, category_name):
    object_list = Post.objects.filter(status='published', category=category)
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/category_list.html', {
        'page': page, 
        'posts': posts, 
        'category_name': category_name
    })


def category_whats_new(request):
    return category_view(request, 'whats_new', "What's New")


def category_funny(request):
    return category_view(request, 'funny', 'Funny')


def category_learning(request):
    return category_view(request, 'learning', 'Learning')


def category_fake_news(request):
    return category_view(request, 'fake_news', 'Fake News')


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             created__year=year,
                             created__month=month,
                             created__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
