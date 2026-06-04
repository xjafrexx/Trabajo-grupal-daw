from django.contrib import admin
# Asegúrate de importar 'include' junto a 'path'
from django.urls import path, include 

urlpatterns = [
    # La ruta del administrador de Django que ya tenías
    path('admin/', admin.site.urls),
    
    # Enlazamos las URLs de tu aplicación applib
    path('', include('WebApps.applib.urls')),
]