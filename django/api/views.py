from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import HttpResponse
from .serializers import BookSerializer
from .models import Book
from django.http import HttpResponse, JsonResponse
import os


import sys
sys.path.insert(1, 'C:\\Users\\HNC\Desktop\\YT-image-upload\\django\\api')
sys.path.insert(1, 'C:\\Users\\HNC\Desktop\\YT-image-upload\\django\\api\\apps.py')


from apps import ApiConfig

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        
        cover = request.data['cover']
        title = request.data['title']
        
        Book.objects.create(title=title, cover=cover)     
        # Book.caption = 'hello'
        # Book.save()
        return HttpResponse({'message': 'son an cut'}, status=200)

class PredictView(APIView):
    def get(self,request):
        if request.method == 'GET' :
            img_path = 'C:\\Users\\HNC\Desktop\\YT-image-upload\\django\\modia\\image.jpg'
            if os.path.exists(img_path):
                text = ApiConfig.getClass.getCap(img_path)
                os.remove(img_path)
            else:
                text = "IMAGE DOESN'T SEND YET"
            
            return JsonResponse({'caption' : text})

