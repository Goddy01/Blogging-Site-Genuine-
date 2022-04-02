from django.shortcuts import render
from operator import attrgetter
from blog.models import BlogPost
# Create your views here.
def home_page(request):
    context = {}
    
    blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'), reverse=True) # Sorts the blog post by their dates, here the latest/newest blog posts will comr first in the list.

    queries = ""
    if request.GET:
        queries = request.GET['query']
    context['queries'] = queries

    context['blog_posts'] = blog_posts
    return render(request, 'blog_app/home.html', context)