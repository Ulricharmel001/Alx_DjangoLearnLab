from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import Library, Book
from .forms import BookForm

# View to display a list of all books in the system.
# Retrieves all Book objects from the database and passes them to the template for rendering.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view that shows detailed information about a specific library.
# Uses Django's DetailView to handle fetching the library by its primary key and passing it to the template.
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# View to handle user registration.
# Uses Django's built-in UserCreationForm to allow users to sign up.
# On successful registration, redirects the user to the login page.
class register(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')


# View to handle user login.
# Extends Django's built-in LoginView.
# Redirects already authenticated users to the book list page.
class LoginView(DjangoLoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True
    success_url =reverse_lazy('list_books')


    # Defines where to redirect users after successful login.
    def get_success_url(self):
        return reverse_lazy('books')


# View to handle user logout.
# Extends Django's built-in LogoutView.
# Optionally can use a template to confirm logout.
class LogoutView(DjangoLogoutView):
    template_name = 'relationship_app/logout.html'


# Helper function to check if the logged-in user has a specific role.
# Returns True if the user has an associated UserProfile and the role matches.
def check_role(user, role):
    return hasattr(user, 'userprofile') and user.userprofile.role == role


# View restricted to users with the 'Admin' role.
# Requires the user to be logged in and pass the role check.
# Renders a template specific to admin users.
@login_required
@user_passes_test(lambda user: check_role(user, 'Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# View restricted to users with the 'Librarian' role.
# Requires the user to be logged in and pass the role check.
# Renders a template specific to librarians.
@login_required
@user_passes_test(lambda user: check_role(user, 'Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# View restricted to users with the 'Member' role.
# Requires the user to be logged in and pass the role check.
# Renders a template specific to members.
@login_required
@user_passes_test(lambda user: check_role(user, 'Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# View to add a new book to the system.
# Only accessible to users with the 'can_add_book' permission.
# On POST request, validates and saves the new book form.
# On GET request, renders an empty form.
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})


# View to edit an existing book.
# Only accessible to users with the 'can_change_book' permission.
# Retrieves the book by primary key and binds it to a form.
# Saves changes if the form is valid.
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'relationship_app/book_form.html', {'form': form})


# View to delete a book from the system.
# Only accessible to users with the 'can_delete_book' permission.
# Confirms deletion via POST request before deleting the book.
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})


# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def redirect_based_on_role(request):
    role = getattr(request.user.userprofile, 'role', None)
    
    if role == 'Admin':
        return redirect('admin_view')
    elif role == 'Librarian':
        return redirect('librarian_view')
    elif role == 'Member':
        return redirect('member_view')
    else:
        return redirect('login')  # fallback
