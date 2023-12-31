from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', views.prueba, name='prueba'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)