from django.urls import path
from .views import (registro, 
                    usuario, 
                    GestionCategorias, 
                    GestionCategoria, 
                    GestionCategoriasGenerico,
                    GestionCategoriaGenerico,
                    GestionPrestamos,
                    GestionLibros)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('registro/',registro),
    # Me devuelve las tokens de acceso a mi API
    path('login/',TokenObtainPairView.as_view()),
    path('perfil', usuario),
    path('categorias',GestionCategorias.as_view()),
    path('categoria/<id>', GestionCategoria.as_view()),
    path('categorias-generic', GestionCategoriasGenerico.as_view()),
    # Al utilizar un generico y este necesite un id para poder funcionar (Retrieve | Update | Destroy) necesitamos pasarle por el parametro el nombre 'pk'
    path('categoria-generic/<pk>', GestionCategoriaGenerico.as_view()),
    path('prestamos',GestionPrestamos.as_view()),
    path('libros', GestionLibros.as_view())
]