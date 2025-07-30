from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import AbstractUser

# Create your models here.

"""
creating relation between author and books, using ForeignKey 
with this , if we delete an Author, we automatically delete all their books as well
"""
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title
"""
creating a library model that relate to book using django ManyToManyField, that is a library can hold many
instance of books and and many book model can be in library
"""

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='books')

    def __str__(self):
        return f"Library : {self.name}, Books :{self.books}"

"""
librarian model that has one-to-one Field relationship with library, this means that if you 
delete a library you delete, the librarian as well

"""
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"Librarian: {self.name}, Library : {self.library}"

        """User profile model """
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"



class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User')


    

    
    
