from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings

class File(models.Model):
    NEW_STATUS = 'new'
    UPDATED_STATUS = 'updated'
    VERIFIED_STATUS = 'verified'

    STATUS = (
        (NEW_STATUS, 'new'),
        (UPDATED_STATUS, 'updated'),
        (VERIFIED_STATUS, 'verified')
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files', validators=[FileExtensionValidator(['py'])])
    status = models.CharField(choices=STATUS, default=NEW_STATUS, max_length=8)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Logs(models.Model):

    file = models.ForeignKey(File, on_delete=models.CASCADE)
    logs = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

