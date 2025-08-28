# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
from .views import CommentDeleteView, CommentUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),  # <-- this MUST exist
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # comments
path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]

