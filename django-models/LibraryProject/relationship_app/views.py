from django.shortcuts import render, redirect
from .models import Book, Library, Librarian, Author
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView



 


# Create your views here.

def list_books(request):
    model =  Book
    """Retrieves all books and renders a template displaying the list."""
    
    books = Book.objects.all()  

    context = {'books': books}  # Create a context dictionary with book list
    
    return render(request, 'list_books.html', {'books' : books})


''' Class base view displays details for a 
specific library, listing all books available in that library.'''
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    


''' Creating user authentication views, register, login and logout'''
class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

class LoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

class LogoutView(LogoutView):
    template_name = 'logout.html'
    success_url = reverse_lazy('login')