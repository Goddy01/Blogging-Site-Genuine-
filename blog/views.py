from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from blog.models import (
    BlogPost
)
# Create your views here.

def create_blog_view(request):
    if not request.user.is_authenticated:
        return redirect ('login')

    return render(request, 'blog/create_blog.html')