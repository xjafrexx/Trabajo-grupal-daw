import uuid
from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .users import User

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    publishYear = models.IntegerField(db_column='publishYear', null=True, blank=True)
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    created_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='books_created', db_column='created_id')
    modified_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='books_modified', db_column='modified_id')

    class Meta:
        db_table = 'books'
        ordering = ['title', 'publishYear']

    def clean(self):
        current_year = datetime.now().year
        if self.publishYear is not None and (self.publishYear < 0 or self.publishYear > current_year):
            raise ValidationError(_('El año de publicación no es válido.'))
        super(Book, self).clean()

    def save(self, *args, **kwargs):
        self.clean()
        self.title = self.title.upper()
        return super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.title, self.publishYear)