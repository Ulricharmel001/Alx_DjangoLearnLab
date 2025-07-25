from django.db import models

# Create your models here.

"""
creating relation between author and books, using ForeignKey 
with this , if we delete an Author, we automatically delete all their books as well
"""
class Author(models.Model):
    author_name = models.CharField(max_length=200)
    def __str__(self):
        return self.author_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

"""
creating a library model that relate to book using django ManyToManyField, that is a library can hold many
instance of books and and many book model can be in library
"""

class Library(models.Model):
    library_name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='books')

"""
librarian model that has one-to-one Field relationship with library, this means that if you 
delete a library you delete, the librarian as well

"""
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
