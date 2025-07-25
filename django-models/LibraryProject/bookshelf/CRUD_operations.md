
# Full CRUD Operations in Django Shell

This document includes all CRUD operations (Create, Retrieve, Update, Delete) performed in the Django shell for the `Book` model.

## CREATE
python command
from books.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984, By: George Orwell, Published in: 1949>

## Rtrieve
book = Book.objects.get(title="1984")
book.title       # Output: '1984'
book.author      # Output: 'George Orwell'
book.publication_year  # Output: 1949

## Update 
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
### Output: 'Nineteen Eighty-Four'

## Delete

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
### Output: <QuerySet []>