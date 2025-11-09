from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Usuario, Categoria, Prestamo, Libro
from django_ulid.serializers import ULIDField

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

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class PrestamoSerializer(ModelSerializer):
    def to_representation(self, instance):
        return {
            'id':str(instance.id),
            'libroId':str(instance.libroId),
            'usuarioId':str(instance.usuarioId),
            'fecha':instance.fecha,
            'estado':instance.estado,
        }
    
    class Meta:
        model= Prestamo
        fields='__all__'

class LibroSerializer(ModelSerializer):
    def to_representation(self, instance):
        
        return {
            'id':str(instance.id), 
            'nombre':instance.nombre,
            'autor': instance.autor,
            'edicion':instance.edicion,
            'descripcion': instance.descripcion,
            'categoriaId': str(instance.categoriaId.id)
                }
    class Meta:
        model = Libro
        fields='__all__'