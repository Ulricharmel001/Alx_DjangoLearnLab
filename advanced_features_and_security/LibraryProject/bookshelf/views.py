from django.shortcuts import render

# Create your views here.


from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book

# View to edit a book (only users with can_edit permission can access)
@permission_required('books.can_edit', raise_exception=True)
def book_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # process form data here...
        # save updates to book
        return redirect('book_detail', book_id=book.id)
    return render(request, 'edit_book.html', {'book': book})


# View to create a book (only users with can_create permission can access)
@permission_required('books.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # process form data and create book
        return redirect('books_list')
    return render(request, 'create_book.html')


# View to delete a book (only users with can_delete permission can access)
@permission_required('books.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books_list')
    return render(request, 'confirm_delete.html', {'book': book})
