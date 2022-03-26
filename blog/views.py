from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import (CreateBlogPostForm,
                    UpdateBlogPostForm
                    )
from account.models import Account
from .models import BlogPost

from blog.models import (
    BlogPost
)
# Create your views here.

def create_blog_view(request):
    """The view to create a blog post"""
    if not request.user.is_authenticated:
        return redirect ('must_auth')
    context = {}

    user = request.user
    create_blog_form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if create_blog_form.is_valid():
        obj = create_blog_form.save(commit=False)
        author = Account.objects.filter(email=user.email).first() # Return a queryset '.first. gets the first item there
        obj.author = author
        obj.save()
        context['success_message'] = f'{obj.title} has been posted.'
        create_blog_form = CreateBlogPostForm()

    context['create_blog_form'] = create_blog_form
    return render(request, 'blog/create_blog.html', context)


def blog_details_view(request, slug):
    """The view to get the details of a blog"""
    context = {}
    blog_details = get_object_or_404(BlogPost, slug=slug)
    context['blog_details'] = blog_details
    return render(request, 'blog/blog_details.html', context)


def update_blog_post_view(request, slug):
    """The view to update a blog post"""
    context = {}
    user = request.user
    if not user.is_authenticated:
        redirect('must_auth')

    blog_post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        update_form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if update_form.is_valid():
            update_form.save()
            context['success_message'] = 'Blog Post has been updated.'

    else:
        update_form = UpdateBlogPostForm(instance=request.user)

    context['blog_post'] = blog_post
    context['update_form'] = update_form
    return render(request, 'blog/edit_blog_post.html', context)