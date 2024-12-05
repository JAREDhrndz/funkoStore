# funko/urls.py
from django.urls import path
from . import views  # Asegúrate de importar las vistas de la aplicación 'funko'

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la vista principal que renderiza 'index.html'
]
