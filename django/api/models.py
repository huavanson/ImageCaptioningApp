from django.db import models
from django_base64field.fields import Base64Field
from django.core.files.base import ContentFile, File


def upload_path(instance, filname='1.jpg'):
    return '/'.join(['covers', str(instance.title), filname])
    #return '/'.join(['covers', filname])


class Book(models.Model):
    title = models.CharField(max_length=32, blank=False)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)
    #cover = models.CharField(max_length=100000000000000000000000, blank=False)
    #cover = Base64Field(max_length=900000, blank=True, null=True)
    #cover = models.FileField(blank=True, upload_to=upload_path)
    #cover = models.base
    

    # def save(self, new_name, new_contents):
    #     self.cover.save(new_name, new_contents)