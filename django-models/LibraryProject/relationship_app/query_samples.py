from .models import Book, Librarian, Library, Author
from django.db import models
# retrieving book by a specific author, assuming "Dan lok" as our author
book = Book.objects.filter(Author='Dan lok')
for book in Book:# for loop
    print(book.title) # displaying all books by Dan lok, using it title


# retrieving book in a given library, in this case i assume, "Library_name" as the given library
Library = Library.objects.get(name=library_name)
book = library.books.all()


# Retrieving librarian of a given library
# first we get the library to retrieve the librarian working there, and its said to be only one per library

library = Library.objects.get(name='my_library')
librarian = library.Librarian


    

