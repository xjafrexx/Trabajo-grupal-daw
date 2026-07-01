import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .users import User

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullName = models.TextField(db_column='fullName')
    nationality = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    created_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='authors_created', db_column='created_id')
    modified_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='authors_modified', db_column='modified_id')

    class Meta:
        db_table = 'authors'
        ordering = ['fullName']

    def clean(self):
        if self.fullName and len(self.fullName.strip()) < 3:
            raise ValidationError(_('El nombre completo del autor debe tener al menos 3 caracteres.'))
        super(Author, self).clean()

    def save(self, *args, **kwargs):
        self.clean()
        self.fullName = self.fullName.upper()
        if self.nationality is not None:
            self.nationality = self.nationality.upper()
        return super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.id, self.fullName)