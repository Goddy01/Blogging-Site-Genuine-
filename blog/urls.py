from django.urls import re_path
from .views import (
    create_blog_view,
    )

app_name = 'blog'

urlpatterns = [
    re_path(r'^create_post/$', create_blog_view, name="create_blog_post")
]