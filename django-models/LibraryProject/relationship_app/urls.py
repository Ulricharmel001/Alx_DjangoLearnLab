from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignupView, LoginView, LogoutView, list_books, LibraryDetailView
from . import views 

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    # Signup using your custom view
    path('register/', SignupView.as_view(), name='register'),
    # Login and Logout using Django built-in auth views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


   
   
    



