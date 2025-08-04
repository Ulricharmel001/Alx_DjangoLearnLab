from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Book views
    path('books/', views.list_books, name='list_books'),
    path('books/add_book/', views.add_book, name='add_book'),
    path('books/edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),

    # Library detail
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('redirect/', views.redirect_based_on_role, name='role_redirect'),

    # User auth views
    path('register/', views.register.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
#  path('accounts/login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    # Role-based dashboards
    path('dashboard/admin/', views.admin_view, name='admin_view'),
    path('dashboard/librarian/', views.librarian_view, name='librarian_view'),
    path('dashboard/member/', views.member_view, name='member_view'),
]
