from rest_framework.decorators import api_view, permission_classes
# IsAuthenticatedOrReadOnly > Si es GET puede acceder sin problemas, sin embargo si no lo es tiene que esta autenticado
# IsAuthenticated > si o si tiene que estar autenticado
# IsAdminUser > solo los usuarios que sean superuser pueden acceder
# AllowAny > Cualquiera puede aceder este o no este autenticado
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer

@api_view(['POST'])
def registro(request):
    print(request.data)
    # Le pasamos la info que queremos validar al serializador
    serializador = UsuarioSerializer(data=request.data)
    
    if serializador.is_valid():
        # Si la informacion es valida entonces podremos obtenerla mediante el atributo validated_data
        print(serializador.validated_data)

        # Ahora procedemos con la creacion del usuario
        nombre = serializador.validated_data.get('nombre')
        correo = serializador.validated_data.get('correo')
        apellido = serializador.validated_data.get('apellido')
        password = serializador.validated_data.get('password')

        nuevoUsuario = Usuario(nombre=nombre, correo=correo, apellido=apellido)
        # generamos el hash de la password
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()

        return Response(data={
            'message':'Usuario registrado exitosamente'
        },status=status.HTTP_201_CREATED)
    else:
        return Response(data={
            'message':'Error al crear el usuario',
            'content':serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    


# si este endpoint es SOLO PARA personas autenticadas
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def usuario(request):
    print(request.auth) # retorna la token si es proveida
    print(request.user) # retorna la instancia de usuario que esta enviando la peticion
    usuarioActual = request.user
    # Cuando queremos convertir informacion de la bd a un diccionario le tenemos que pasar el parametro instance, sin embargo, si la queremos validar la data para guardar, usaremos el parametro data
    serializador = UsuarioSerializer(instance = usuarioActual)
    
    return Response(data={
        'content':serializador.data
    })