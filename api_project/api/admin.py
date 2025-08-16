from django.contrib import admin
from .models import Book

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')  # fields to show in the admin list view
    search_fields = ('title', 'author')       # fields to search by
