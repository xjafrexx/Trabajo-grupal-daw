from django.contrib import admin

from .models.books import Book
from .models.authors import Author
from .models.authors_books import AuthorBook
from .models.book_copies import BookCopy
from .models.books_categories import BookCategory
from .models.categories import Category
from .models.loans import Loan
from .models.users import User

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(AuthorBook)
admin.site.register(BookCopy)
admin.site.register(BookCategory)
admin.site.register(Category)
admin.site.register(Loan)
admin.site.register(User)