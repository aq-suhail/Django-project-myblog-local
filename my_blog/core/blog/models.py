from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager 
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    options =(
        ("draft", "Draft"),
        ("published", "Published")
    )


    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    image = models.ImageField(upload_to='./blog_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=10, choices=(('draft', 'Draft'), ('published', 'Published')), default='draft')
    tags = TaggableManager() 

    def get_absolute_url(self):
        return reverse("post_single", args={self.slug})
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class Imageslides(models.Model):
    
    slide_image = models.ImageField(upload_to='./slide_images/', blank=True)
    status = models.CharField(max_length=10, choices=(('draft', 'Draft'), ('published', 'Published')), default='draft')
    count = models.IntegerField(default=0)
    published_at = models.DateTimeField(default=timezone.now)

   