from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api.views import BookViewSet, PredictView
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('books', BookViewSet)
#router.register('api/predict', PredictViewSet, 'predict')
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('getCaption/', PredictView.as_view())

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)