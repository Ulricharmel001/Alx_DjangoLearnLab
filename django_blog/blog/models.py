from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Blog Post model
class Post(models.Model):
    title = models.CharField(max_length=200)  # Blog title
    content = models.TextField()  # Blog content/body
    published_date = models.DateTimeField(auto_now_add=True)  # Auto timestamp
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    # Each post belongs to a user (author). If user is deleted, their posts are deleted too.

    def __str__(self):
        return self.title  # Display post title in admin panel


# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Redirect to post detail page after creating/updating
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
