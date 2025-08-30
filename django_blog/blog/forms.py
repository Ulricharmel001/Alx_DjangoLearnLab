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
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # ✅ include tags
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Write your post...'}),
        }
        help_texts = {
            'tags': "Add comma-separated tags (e.g. django, python, web)."
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
