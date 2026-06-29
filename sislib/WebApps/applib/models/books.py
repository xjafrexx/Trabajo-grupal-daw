import uuid
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError 
from .users import User

def validate_publish_year(value):
    if value > timezone.now().year:
        raise ValidationError('El año de publicación no puede ser en el futuro.')

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    publishYear = models.IntegerField(
        db_column='publishYear', 
        null=True, 
        blank=True, 
        validators=[validate_publish_year]
    )
    
    status = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    created_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='books_created', db_column='created_id')
    modified_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='books_modified', db_column='modified_id')

    authors = models.ManyToManyField(
        'Author', 
        through='AuthorBook', 
        related_name='books'
    )

    categories = models.ManyToManyField(
        'Category',
        through='BookCategory',
        related_name='books'
    )

    class Meta:
        db_table = 'books'

    def __str__(self):
        return f"{self.title} ({self.publishYear})"

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        super().save(*args, **kwargs)