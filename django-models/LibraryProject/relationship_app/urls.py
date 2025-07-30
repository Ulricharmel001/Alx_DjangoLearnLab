from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignupView, LoginView, LogoutView, list_books, LibraryDetailView
from .views import list_books, register
from . import views

from django.urls import path
from .views import admin_view, librarian_view, member_view


   


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # Signup using your custom view
    path('register/', views.register, name='register'),
    # Login and Logout using Django built-in auth views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout'), name='logout'),
    path('admin-page/', views.admin_view, name='admin_view'),
    path('librarian-page/', views.librarian_view, name='librarian_view'),
    path('member-page/', views.member_view, name='member_view'),
     path('admin-role/', admin_view.admin_view, name='admin-view'),
    path('librarian-role/', librarian_view.librarian_view, name='librarian-view'),
    path('member-role/', member_view.member_view, name='member-view'),
    path('books/add_book/', views.add_book, name='add_book'),
    path('books/edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]
    

    

    