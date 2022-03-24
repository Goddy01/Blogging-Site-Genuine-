from venv import create
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateBlogPostForm
from account.models import Account

from blog.models import (
    BlogPost
)
# Create your views here.

def create_blog_view(request):
    if not request.user.is_authenticated:
        return redirect ('must_authenticate')
    context = {}

    user = request.user
    create_blog_form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if create_blog_form.is_valid():
        obj = create_blog_form.save(commit=False)
        author = Account.objects.filter(email=user.email)[1]
        obj.author = author
        obj.save()
        create_blog_form = CreateBlogPostForm()
    
    context['create_blog_form'] = create_blog_form
    return render(request, 'blog/create_blog.html')