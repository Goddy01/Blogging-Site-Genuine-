from django.shortcuts import render
from operator import attrgetter
from blog.models import BlogPost
from blog.views import get_blog_queryset
# Create your views here.
def home_page(request):
    context = {}
    
    query = ""
    if request.GET:
        query = request.GET['query']
        context['query'] = str(query)

    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True) # Sorts the blog post by their dates, here the latest/newest blog posts will comr first in the list.

    context['blog_posts'] = blog_posts
    return render(request, 'blog_app/home.html', context)