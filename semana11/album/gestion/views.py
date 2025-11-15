from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Album, Archivo, Recuerdo
from .serializers import AlbumSerializer

class GestionAlbumn(ListCreateAPIView):
    # Asi indicamos que solo vamos a listar los albumnes cuyo finalizado sea True
    queryset = Album.objects.filter(finalizado=True).all()
    serializer_class = AlbumSerializer


@api_view(http_method_names=['PUT'])
def alternarAlbumEstado(request, id):
    # En base al id que tengamos por la url `/alternar-estado-albumn/123abc`
    # modificar el valor de finalizado y si es verdadero ponerlos a falso y viceversa
    albumEncontrado = Album.objects.filter(id=id).first()
    if not albumEncontrado:
        return Response(data={
            'message':'Album no encontrado'
        },status=status.HTTP_400_BAD_REQUEST)
    
    # Por ser un boolean podemos alternar el valor del finalizado con la palabra `not`
    albumEncontrado.finalizado = not albumEncontrado.finalizado

    albumEncontrado.save()
    result = AlbumSerializer(instance=albumEncontrado)

    return Response(data={
        'message':'Estado modificado exitosamente',
        'content':result.data
    })
