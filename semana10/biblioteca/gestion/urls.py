from django.urls import path
from .views import registro, usuario
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('registro/',registro),
    # Me devuelve las tokens de acceso a mi API
    path('login/',TokenObtainPairView.as_view()),
    path('perfil', usuario)
]