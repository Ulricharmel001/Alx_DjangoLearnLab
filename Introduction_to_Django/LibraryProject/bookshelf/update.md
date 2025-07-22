# ✏️ Update Operation

python command:

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# Output: 'Nineteen Eighty-Four'
book
<Book: Nineteen Eighty-Four, By: George Orwell, Published in: 1949>
