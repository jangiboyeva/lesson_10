from django.core.validators import FileExtensionValidator
from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=250)
    video = models.FileField(upload_to='massages/video/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'ogg', 'avi', 'wmv'])
    ])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name