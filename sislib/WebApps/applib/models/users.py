import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.TextField(db_column='firstName')
    lastName = models.TextField(db_column='lastName')
    email = models.EmailField(unique=True)
    isAdmin = models.BooleanField(default=False, db_column='isAdmin')
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    created_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='users_created', db_column='created_id')
    modified_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='users_modified', db_column='modified_id')

    class Meta:
        db_table = 'users'
        ordering = ['lastName', 'firstName', 'email']

    def clean(self):
        if self.email and "@" not in self.email:
            raise ValidationError(_('El formato del correo electrónico no es válido.'))
        super(User, self).clean()

    def save(self, *args, **kwargs):
        self.clean()
        self.firstName = self.firstName.upper()
        self.lastName = self.lastName.upper()
        if self.email:
            self.email = self.email.lower()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s" % (self.lastName, self.firstName, self.email)