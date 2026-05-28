import uuid
from django.db import models
from django.utils import timezone
from .users import User

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoryName = models.TextField(db_column='categoryName')
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    created_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='categories_created', db_column='created_id')
    modified_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='categories_modified', db_column='modified_id')

    class Meta:
        db_table = 'categories'