from django.shortcuts import get_list_or_404, render, redirect
from .forms import CreateBlogPostForm
from account.models import Account
from .models import BlogPost

from blog.models import (
    BlogPost
)
# Create your views here.

def create_blog_view(request):
    if not request.user.is_authenticated:
        return redirect ('must_auth')
    context = {}

    user = request.user
    create_blog_form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if create_blog_form.is_valid():
        obj = create_blog_form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        create_blog_form = CreateBlogPostForm()
    
    context['create_blog_form'] = create_blog_form
    return render(request, 'blog/create_blog.html')


def blog_detail_view(request, slug):
    context = {}
    blog_details = get_list_or_404(BlogPost, slug=slug)
    context['blog_details'] = blog_details
    return render(request, 'blog/blog_details.html')