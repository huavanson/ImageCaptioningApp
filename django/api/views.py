from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import BookSerializer
from .models import Book
from PIL import Image
from rest_framework.permissions import IsAuthenticated, AllowAny
import matplotlib.pyplot as plt
import io

import base64
from django.core.files.base import ContentFile

def base64_file(base64_string, name='1'):
    format, imgstr = base64_string.split(';base64,')
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name=name + "." + ext)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        title = request.data['title']
        #Book.objects.create(title=title, cover=base64_file(cover))
        newbook = Book()
        newbook.title = title
        newbook.cover = base64_file(cover)
        newbook.save()

        # image_data = base64.b64decode(book.cover)
        # my_model_instance.cool_image_field = ContentFile(image_data, 'C:\\Users\\HNC\\Desktop\\YT-image-upload\\django\\modia\\covers\\mother\\whatup.jpg')
        # my_model_instance.save()
        #book.save(new_name='C:\\Users\\HNC\\Desktop\\YT-image-upload\\django\\modia\\covers\\mother\\oke.jpg', new_contents=book.cover)
        return HttpResponse({'message': 'Book created'}, status=200)