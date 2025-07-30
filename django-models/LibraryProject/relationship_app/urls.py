from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignupView, LoginView, LogoutView, list_books, LibraryDetailView
from .views import list_books, register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # Signup using your custom view
    path('register/', register.as_view(), name='register'),
    # Login and Logout using Django built-in auth views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout'), name='logout'),

]
   
   
    



