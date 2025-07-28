from . import views
from django.urls import path

from django.urls import path
from django.contrib.auth import views as auth_views
from . views import LoginView, LogoutView, SignupView



urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(),  name='library_detail'),
    path('sigup/', views.SignupView.as_view(), name ='signup' ),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logut')


   
   
    

]

