from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings 
from django.db.models.signals import post_delete
from django.dispatch import receiver


def upload_location(instance, filename):
    """Generate the file path for image upload"""
    file_path = f'blog/{str(instance.author.id)}/{str(instance.title)}-{filename}'
    return file_path

class BlogPost(models.Model):
    """Creates these fields in the database which will be the attributes of a post"""
    title                   = models.Charield(max_length=50, blank=False, null=False)
    body                    = models.TextField(maxx_length=5000, blank=False, null=False)
    image                   = models.ImageField(upload_to=upload_location, blank=False, null=False)
    date_published          = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated            = models.DateTimeField(auto_add=True, verbose_name="date updated")
    author                  = models.ForeignKey(settings.AUTH.UAER_MODEL, on_delete=models.CASCADE)
    slug                    = models.SlugField(blank=True, unique=True)

    
    def __str__(self):
        return self.title
