from rest_framework.decorators import api_view, permission_classes
# IsAuthenticatedOrReadOnly > Si es GET puede acceder sin problemas, sin embargo si no lo es tiene que esta autenticado
# IsAuthenticated > si o si tiene que estar autenticado
# IsAdminUser > solo los usuarios que sean superuser pueden acceder
# AllowAny > Cualquiera puede aceder este o no este autenticado
from rest_framework.permissions import  IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .permissions import EsAdmin, EsPersonal
from .models import Usuario, Categoria, Prestamo, Libro
from .serializers import UsuarioSerializer, CategoriaSerializer, PrestamoSerializer, LibroSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView


    

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
        tipoUsuario = serializador.validated_data.get('tipoUsuario')

        nuevoUsuario = Usuario(nombre=nombre, correo=correo, apellido=apellido, tipoUsuario = tipoUsuario)
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

class GestionCategorias(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, EsAdmin]

    def get(self, request):
        # SELECT * FROM categorias;
        categorias = Categoria.objects.all()
        # Cuando las instancia es mas de una entonces declaramos el parametro many=True
        resultado = CategoriaSerializer(instance=categorias, many=True)

        return Response(data={
            'message':'Las categorias son',
            'content': resultado.data
        })
    
    def post(self,request):
        # Si queremos validar la informacion usaremos el parametro data
        serializador = CategoriaSerializer(data=request.data)

        if serializador.is_valid():
            nuevaCategoria = Categoria(**serializador.validated_data)

            nuevaCategoria.save()

            # Si queremos mostrar la informacion desde una instancia usaremos el parametro instance
            resultado = CategoriaSerializer(instance=nuevaCategoria)
            return Response(data={
                'message':'Categoria creada exitosamente',
                'content': resultado.data
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response(data={
                'message':'Error al crear la categoria',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
class GestionCategoria(APIView):
    def get(self, request, id):
        # SELECT * FROM categorias WHERE id = ... LIMIT 1
        categoriaEncontrada = Categoria.objects.filter(id=id).first()

        if not categoriaEncontrada:
            return Response(data={
                'message':'Categoria no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategoriaSerializer(instance=categoriaEncontrada)

        return Response(data={
            'content': serializer.data
        })
    
    def put(self,request,id):
        categoriaEncontrada = Categoria.objects.filter(id=id).first()

        if not categoriaEncontrada:
            return Response(data={
                'message':'Categoria no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            # Aca hago las actualizaciones de los campos
            categoriaEncontrada.nombre = serializer.validated_data.get('nombre')
            # Ahora guardamos las modificaciones de manera permanente
            categoriaEncontrada.save()

            resultado = CategoriaSerializer(instance=categoriaEncontrada)

            return Response(data={
                'message':'Categoria actualizada exitosamente',
                'content': resultado.data
            })
        
        else:
            return Response(data={
                'message':'Error al actualizar la categoria',
                'content':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        categoriaEncontrada = Categoria.objects.filter(id=id).first()

        if not categoriaEncontrada:
            return Response(data={
                'message':'Categoria no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # DELETE FROM categorias WHERE id = ....
        Categoria.objects.filter(id=id).delete()

        return Response(data={
            'message':'Categoria eliminada exitosamente'
        })

# Ahora usando vistas genericas logica
class GestionCategoriasGenerico(ListCreateAPIView):
    # Es la consulta que usara la clase generica para poder acceder a la data de la bd
    queryset = Categoria.objects.all()

    # Es el serializador que usara para poder validar y devolver la data
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, EsAdmin]
    
class GestionCategoriaGenerico(RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, EsAdmin]
    # si usamos:
    # Retrieve > retrieve
    # List > list
    # Update > update
    # Destry > destroy
    def destroy(self,request,pk):
        # asi podemos alterar el comportamiento 'natural' de los genericos
        categoriaEncontrada = Categoria.objects.filter(id=pk).first()

        if not categoriaEncontrada:
            return Response(data={
                'message':'Categoria no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # DELETE FROM categorias WHERE id = ....
        Categoria.objects.filter(id=pk).delete()

        return Response(data={
            'message':'Categoria eliminada exitosamente'
        })

class GestionPrestamos(ListCreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, EsPersonal]

class GestionLibros(ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, EsAdmin]