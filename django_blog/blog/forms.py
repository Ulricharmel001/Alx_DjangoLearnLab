# blog/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Author will be assigned automatically in view





from django import forms
from .models import Comment

# Form to create or update a comment
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Write a comment...'
        }),
        label=''  # Hide the default label
    )

    class Meta:
        model = Comment
        fields = ['content']  # Only the content field is editable; post and author are set in view
