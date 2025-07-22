# Delete Opeartion

python command:
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Output: <QuerySet []> (book has been deleted)
