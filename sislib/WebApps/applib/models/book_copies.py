import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .users import User
from .books import Book

class BookCopy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, db_column='book_id')
    copyNumber = models.IntegerField(db_column='copyNumber')
    barcode = models.TextField(unique=True)
    physicalCondition = models.TextField(db_column='physicalCondition', default='BUENO', null=True, blank=True)
    is_available = models.BooleanField(default=True, null=False)
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    created_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='copies_created', db_column='created_id')
    modified_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='copies_modified', db_column='modified_id')

    class Meta:
        db_table = 'book_copies'
        ordering = ['book', 'copyNumber']
        constraints = [
            models.UniqueConstraint(fields=['book', 'copyNumber'], name='unique_book_copy')
        ]

    def clean(self):
        if self.copyNumber is not None and self.copyNumber <= 0:
            raise ValidationError(_('El número de copia debe ser un entero positivo.'))
        super(BookCopy, self).clean()

    def save(self, *args, **kwargs):
        self.clean()
        if self.physicalCondition is not None:
            self.physicalCondition = self.physicalCondition.upper()
        if self.barcode:
            self.barcode = self.barcode.upper()
        return super(BookCopy, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.book, self.copyNumber)