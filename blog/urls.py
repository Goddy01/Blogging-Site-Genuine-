from django.urls import re_path, path
from .views import (
    create_blog_view, blog_details_view
    )

app_name = 'blog'

urlpatterns = [
    re_path(r'^create_post/$', create_blog_view, name="create_blog_post"),
    path('<slug>', blog_details_view, name="blog_details"),
]