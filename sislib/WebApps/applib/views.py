from django.views.generic import ListView, DetailView
from .models import Book, Author, User
class BookListView(ListView):
    model = Book
    template_name = 'applib/book_list.html'
    context_object_name = 'libros'

class BookDetailView(DetailView):
    model = Book
    template_name = 'applib/book_detail.html'
    context_object_name = 'libro'

class AuthorListView(ListView):
    model = Author
    template_name = 'applib/author_list.html'
    context_object_name = 'autores'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'applib/author_detail.html'
    context_object_name = 'autor'

class UserListView(ListView):
    model = User
    template_name = 'applib/user_list.html'
    context_object_name = 'usuarios'

class UserDetailView(DetailView):
    model = User
    template_name = 'applib/user_detail.html'
    context_object_name = 'usuario'