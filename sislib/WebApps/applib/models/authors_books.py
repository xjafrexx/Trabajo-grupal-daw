import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .users import User
from .authors import Author
from .books import Book

class AuthorBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='author_id')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    created_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='auth_books_created', db_column='created_id')
    modified_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='auth_books_modified', db_column='modified_id')

    class Meta:
        db_table = 'authors_books'
        ordering = ['book', 'author']
        constraints = [
            models.UniqueConstraint(fields=['author', 'book'], name='unique_author_book')
        ]

    def clean(self):
        if not self.author.status:
            raise ValidationError(_('No se puede asociar un autor inactivo.'))
        if not self.book.status:
            raise ValidationError(_('No se puede asociar un libro inactivo.'))
        
        duplicate_check = AuthorBook.objects.filter(author=self.author, book=self.book).exclude(id=self.id)
        if duplicate_check.exists():
            raise ValidationError(_('Este autor ya está asignado a este libro.'))
            
        super(AuthorBook, self).clean()

    def save(self, *args, **kwargs):
        self.clean()
        return super(AuthorBook, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.book, self.author)