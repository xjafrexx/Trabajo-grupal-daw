import uuid
from datetime import timedelta
from django.db import models
from django.utils import timezone
from .users import User
from .book_copies import BookCopy

def get_default_due_date():
    return timezone.now().date() + timedelta(days=14)

class Loan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, db_column='user_id')
    book_copy = models.ForeignKey(BookCopy, on_delete=models.RESTRICT, db_column='book_copy_id')
    loanDate = models.DateField(db_column='loanDate', default=timezone.now)
    dueDate = models.DateField(db_column='due_date', default=get_default_due_date)
    loanStatus = models.TextField(db_column='loan_status', default='Activo')
    notes = models.TextField(db_column='notes', null=True, blank=True)
    returnDate = models.DateField(db_column='returnDate', null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    created_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='loans_created', db_column='created_id')
    modified_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='loans_modified', db_column='modified_id')

    class Meta:
        db_table = 'loans'