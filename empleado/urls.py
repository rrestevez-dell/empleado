from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #Incluimos las url de mis app
    path('', include('applications.home.urls')),
    path('', include('applications.empleado.urls')),
    path('', include('applications.departamento.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
