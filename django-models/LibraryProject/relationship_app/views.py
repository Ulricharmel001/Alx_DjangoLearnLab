from .models import Library 
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import  Library, Book
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView

from django.contrib.auth import login



 


# Create your views here.
#"""Retrieves all books and renders a template displaying the list and author."""
  
    
   # List all books with their authors
def list_books(request):
    model = Book
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


''' Class base view displays details for a 
specific library, listing all books available in that library.'''
# View for library detail with list of books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html' 
    context_object_name = 'library'



''' Creating user authentication views, register, login and logout'''
# Signup/Register View using built-in UserCreationForm
class register(CreateView):
    form_class = UserCreationForm()
    template_name = 'relationship_app/register.html'  
    success_url = reverse_lazy('login')  # Redirect to login page after successful signup


#Login View using Django's built-in view
class LoginView(DjangoLoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True
    # NOTE: success_url doesn't work here unless you override get_success_url()

    def get_success_url(self):
        return reverse_lazy('books')  # redirect after login


# Logout View using Django's built-in view
class LogoutView(DjangoLogoutView):
    template_name = 'relationship_app/logout.html'  # optional; you can redirect to login or home

def check_role(role):
    def decorator(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return decorator

@login_required
@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'member_view.html')
