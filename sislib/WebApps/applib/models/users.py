import uuid
from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.TextField(db_column='firstName')
    lastName = models.TextField(db_column='lastName')
    email = models.EmailField(unique=True)
    #isAdmin
    isAdmin = models.BooleanField(default=False, db_column='isAdmin') 
    status = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    created_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='users_created', db_column='created_id')
    modified_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='users_modified', db_column='modified_id')

    class Meta:
        db_table = 'users'