from django.urls import path
from .views import mostrarNotas

# urlpatterns es la variable encargada de mapear todas nuestas rutas de la aplicacion
urlpatterns = [
    path('notas/', mostrarNotas)
]
