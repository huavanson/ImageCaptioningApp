from django.db import models
from django.core.files.base import ContentFile, File


def upload_path(instance, filname):
    return '/'.join(['image.jpg'])


class Book(models.Model):
    title = models.CharField(max_length=32, blank=False)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)

    