import uuid
from django.db import models
from django.utils import timezone
from .users import User
from .books import Book
from .categories import Category

class BookCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')
    status = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    created_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='book_cats_created', db_column='created_id')
    modified_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='book_cats_modified', db_column='modified_id')

    class Meta:
        db_table = 'books_categories'