# Delete Opeartion
from bookshelf.models import Book

python command:
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Output: <QuerySet []> (book has been deleted)