from flask_restful import Resource, request
from cloudinary import utils
from datetime import datetime
from os import environ
from .serializer import GenerarLinkSerializer, ActualizarFotoUsuarioSerializer
from marshmallow import ValidationError
from ..usuarios import UsuarioModel
from .model import MultimediaModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4

from bd import conexion


class GenerarLinkDeFoto(Resource):
    @jwt_required()
    def post(self):
        # generaremos una url firmada para que puedan subir imagenes a nuestro cloudinary basandonos en configuraciones
        serializador = GenerarLinkSerializer()
        try:
            dataValidada = serializador.load(request.get_json())
            timestamp = round(datetime.now().timestamp())
            parametros = {
                # timestamp sirve para validar la hora en la cual ah sido creado la firma
                'timestamp': timestamp,
                # folder serviria por si queremos guardar en una carpeta en especifico nuestro archivo
                'folder': dataValidada.get('folder'),
                # public_id es el nombre del archivo con el que se guardara y hara la validacion que al momento de subirlo sea el mismo nombre de archivo, si es diferente lanzara un error
                # TODO
                # Agregar al public_id un identificador unico (UUID)
                # uuid4()
                'public_id': 'asdadadadsa'+dataValidada.get('fileName')
            }

            signature = utils.api_sign_request(
                parametros, environ.get('CLOUDINARY_API_SECRET'))
            apiKey = environ.get('CLOUDINARY_API_KEY')
            cloudName = environ.get('CLOUDINARY_NAME')
            folder = dataValidada.get('folder')
            cloudinaryUrl = 'https://api.cloudinary.com/v1_1'

            return {
                'content': {
                    'signature': signature,
                    'timestamp': timestamp,
                    'apiKey': apiKey,
                    'url': f'{cloudinaryUrl}/{cloudName}/image/upload',
                    'folder': folder,
                    # TODO
                    # devolver el public id que seria el fileName con el uuid
                    'public_id': ''
                }
            }
        except ValidationError as error:
            return {
                'message': 'Error al generar el link',
                'content': error.args
            }, 400


class ActualizarFotoUsuario(Resource):
    @jwt_required()
    def put(self):
        usuarioId = get_jwt_identity()
        # TODO: Cuando yo actualice mi imagen si el usuario ya tiene una imagen en la tabla multimedias, entonces actualizar el registro, caso contrario crearlo

        # Primero crear un serializador llamado ActualizarFotoUsuarioSerializer
        serializer = ActualizarFotoUsuarioSerializer()
        # usuarioId
        # folder
        # fileName
        # extension
        # contentType
        try:
            data = request.get_json()
            data['usuarioId'] = usuarioId
            dataValidada = serializer.load(data)
            # Validar si el usuario existe y esta validado
            usuarioId = dataValidada.get('usuarioId')

            # SELECT id FROM usuarios WHERE id = '...' AND validado = true;
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter(
                UsuarioModel.id == usuarioId, UsuarioModel.validado == True).with_entities(UsuarioModel.id).first()

            if not usuarioEncontrado:
                return {
                    'message': 'Usuario no existe'
                }, 400

            # Crear un registro en la tabla multimedias y agregar el usuarioId
            nuevaMultimedia = MultimediaModel(**dataValidada)
            conexion.session.add(nuevaMultimedia)

            conexion.session.commit()
            resultado = serializer.dump(nuevaMultimedia)

            return {
                'message': 'Foto actualizada exitosamente',
                'content': resultado
            }, 201

        except ValidationError as error:
            return {
                'message': 'Error al actualizar la foto del usuario',
                'content': error.args
            }, 400


class DevolverMultimediaUrl(Resource):
    @jwt_required()
    def get(self, nombreImagen):
        parametros = {
            'source': 'pruebas/'+nombreImagen,
            'cloud_name': environ.get('CLOUDINARY_NAME'),
            'resource_type': 'image',
            'secure': True,
            # opcionalmente podemos agregar transformaciones a las imagenes
            'transformation': [{'width': 400, 'height': 400, 'crop': 'fill', 'effect': "vignette"}]
        }

        resultado = utils.cloudinary_url(**parametros)

        return {
            'url': resultado[0]
        }
