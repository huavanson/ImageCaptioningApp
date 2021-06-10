from rest_framework import serializers
from .models import Book
#from drf_extra_fields.fields import Base64ImageField

class BookSerializer(serializers.HyperlinkedModelSerializer):
    #image = Base64ImageField()
    class Meta:
        model = Book
        #fields = ['title', 'cover']
        fields = ['title', 'cover']
        #fields = ['cover']