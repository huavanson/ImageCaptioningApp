from django.apps import AppConfig
from api.imageCaptioning.getCap import getCaption



import sys
sys.path.insert(1, 'C:\\Users\\HNC\Desktop\\YT-image-upload\\django\\api\\imageCaptioning')
sys.path.insert(1, 'C:\\Users\\HNC\Desktop\\YT-image-upload\\django\\api\\imageCaptioning\\models.py')

class ApiConfig(AppConfig):
    name = 'api'
  
    getClass = getCaption()

