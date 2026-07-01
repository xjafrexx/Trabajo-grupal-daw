import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .users import User

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoryName = models.TextField(db_column='categoryName')
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    created_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='categories_created', db_column='created_id')
    modified_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='categories_modified', db_column='modified_id')

    class Meta:
        db_table = 'categories'
        ordering = ['categoryName']

    def clean(self):
        if self.categoryName and len(self.categoryName.strip()) < 3:
            raise ValidationError(_('El nombre de la categoría debe tener al menos 3 caracteres.'))
        super(Category, self).clean()

    def save(self, *args, **kwargs):
        self.clean()
        self.categoryName = self.categoryName.upper()
        if self.description is not None:
            self.description = self.description.upper()
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.id, self.categoryName)