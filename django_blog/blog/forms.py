# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class RegisterForm(UserCreationForm):
    """
    Simple register form that also collects email.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class PostForm(forms.ModelForm):
    """
    Post form. 'tags' comes from taggit and accepts comma-separated input.
    """
    from django import forms
from .models import Post
from taggit.forms import TagWidget  # <-- add this

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # added tags field
        widgets = {
            'tags': TagWidget(),  
        }


class CommentForm(forms.ModelForm):
    """
    Minimal comment form.
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write a comment...'}),
        }
