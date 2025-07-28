from django.contrib import admin
from .models import Library, Book  , Author, Librarian


admin.site.register(Library)  # Register Library
# admin.site.register(Book)     # Register Book
admin.site.register(Author)
admin.site.register(Librarian)

class BookAdmin(admin.ModelAdmin):
    list_display =('title', 'author')
    fields = ('title', 'author', 'publicaton_year')
    
admin.site.register(Book)