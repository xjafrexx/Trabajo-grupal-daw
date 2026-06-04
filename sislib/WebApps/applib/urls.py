from django.urls import path
from .views import (
    BookListView, BookDetailView, 
    AuthorListView, AuthorDetailView,
    UserListView, UserDetailView
)

urlpatterns = [
    # Libros
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<uuid:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # Autores
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<uuid:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    
    # Usuarios (Nuevas rutas)
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetailView.as_view(), name='user-detail'),
]