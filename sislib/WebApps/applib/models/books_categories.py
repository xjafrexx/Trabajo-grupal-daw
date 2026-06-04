import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .users import User
from .books import Book
from .categories import Category

class BookCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    created_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='book_cats_created', db_column='created_id')
    modified_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='book_cats_modified', db_column='modified_id')

    class Meta:
        db_table = 'books_categories'
        ordering = ['book', 'category']
        constraints = [
            models.UniqueConstraint(fields=['book', 'category'], name='unique_book_category')
        ]

    def clean(self):
        if not self.book.status:
            raise ValidationError(_('No se puede asociar una categoría a un libro inactivo.'))
        if not self.category.status:
            raise ValidationError(_('No se puede asociar una categoría inactiva a un libro.'))
        
        duplicate_check = BookCategory.objects.filter(book=self.book, category=self.category).exclude(id=self.id)
        if duplicate_check.exists():
            raise ValidationError(_('Esta categoría ya está asignada a este libro.'))
            
        super(BookCategory, self).clean()

    def save(self, *args, **kwargs):
        self.clean()
        return super(BookCategory, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.book, self.category)
