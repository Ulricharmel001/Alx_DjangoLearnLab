from relationship_app.models import Book, Librarian, Library, Author
from django.db import models
# retrieving book by a specific author, 
def BookByAuthor(self):
    author = Author.objects.get(name=author_name)
    author_books = Book.objects.filter(author=author) # Retrieves all books by the author
        


# retrieving book in a given library, in this case i assume, "Library_name" as the given library
library = Library.objects.get(name=library_name)
book = library.books.all()


# Retrieving librarian of a given library
# first we get the library to retrieve the librarian working there, and its said to be only one per library

library = Library.objects.get(name='my_library')
librarian = library.Librarian


    

