from django.urls import path
from .views import GestionAlbumn, alternarAlbumEstado

urlpatterns = [
    path('album', GestionAlbumn.as_view()),
    path('alternar-album-estado/<id>',alternarAlbumEstado),
]