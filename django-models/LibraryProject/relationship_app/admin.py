from django.contrib import admin
from .models import Library, Book  , Author, Librarian


admin.site.register(Library)  # Register Library
# admin.site.register(Book)     # Register Book
admin.site.register(Author)    # Register Author
admin.site.register(Librarian)  # Register Librarian

class BookAdmin(admin.ModelAdmin):
    list_display =('title', 'author')
    fields = ('title', 'author', 'publication_year')
    
admin.site.register(Book)