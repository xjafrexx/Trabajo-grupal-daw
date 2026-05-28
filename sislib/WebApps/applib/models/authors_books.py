import uuid
from django.db import models
from django.utils import timezone
from .users import User
from .authors import Author
from .books import Book

class AuthorBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='author_id')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    status = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    created_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='auth_books_created', db_column='created_id')
    modified_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='auth_books_modified', db_column='modified_id')

    class Meta:
        db_table = 'authors_books'