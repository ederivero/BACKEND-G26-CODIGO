from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(ModelSerializer):
    # password = serializers.CharField(write_only=True)
    class Meta:
        model = Usuario
        # campos vamos a validar 
        # fields = ['id','nombre','correo']
        # si quisieramos usar todos los campos del modelo
        # fields ='__all__'

        # si quisieramos omitir uno o dos campos
        exclude = ['groups', 'user_permissions','is_staff','is_active','is_superuser', 'last_login']
        # NO SE PUEDE USAR EL fields Y EL exclude al mismo tiempo, o es uno o es el otro

        # Son configuraciones adicionales que se le puede colocar a los atributos del modelo
        extra_kwargs={
            'password': {
                'write_only':True
            }
        }