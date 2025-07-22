# Create operation with Django shell 
<!-- creating book object -->
from bookshell.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output:<Book: 1984, By: George Orwell, Published in: 1949>

 <!-- Output of the operation   -->
 Print(book)
 <!-- Output -->
 1984, By: George Orwell, Published in: 1949
 book.title
 <!-- output -->
 1984
 book.author
 <!-- Output -->
 Orwell Goerge
 book.publication_year
 <!-- Output -->
 1949
