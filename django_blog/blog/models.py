from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.


# Blog Post model
# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager  

class Post(models.Model):
    """
    Blog post model. Each post belongs to a user (author).
    """
    title = models.CharField(max_length=200)                 # post title
    content = models.TextField()                             # post body
    published_date = models.DateTimeField(auto_now_add=True) # timestamp on create
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # ✅ Taggable manager adds an m2m relation through taggit tables.
    #    'blank=True' lets you save posts without tags.
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Where to go after create/update — the post detail page.
        """
        return reverse('post_detail', kwargs={'pk': self.pk})


# Comment model to store comments on posts
class Comment(models.Model):
    # Link comment to a specific post; many comments can belong to one post
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    
    # Link comment to the user who wrote it
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # The actual text content of the comment
    content = models.TextField()
    
    # Timestamp when the comment was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Timestamp when the comment was last updated
    updated_at = models.DateTimeField(auto_now=True)

    # String representation of the comment
    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'





