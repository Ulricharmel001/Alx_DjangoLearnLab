from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your models here.

"""
creating relation between author and books, using ForeignKey 
with this , if we delete an Author, we automatically delete all their books as well
"""
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.DateField()
    
    def __str__(self):
        return F"Book Title: {self.title}, Author: {self.author}"
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
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=200, choices=ROLE_CHOICES)
    def __str__(self):
        return f'{self.user}, {self.role}'
    

# in models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User')


    

    
    
