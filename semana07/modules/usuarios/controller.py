from flask_restful import request, Resource
from marshmallow.exceptions import ValidationError
from bcrypt import gensalt, hashpw
from .serializer import RegistrarUsuarioSerializer, HabilitarUsuarioSerializer
from .model import UsuarioModel
from bd import conexion
from utils import enviarCorreoDeValidacion
from cryptography.fernet import Fernet
from os import environ
from ast import literal_eval


class RegistrarUsuario(Resource):
    serializer = RegistrarUsuarioSerializer()

    def post(self):
        data = request.get_json()
        try:

            dataSerializada = self.serializer.load(data)
            # Para generar el hash de nuestra password generamos el salt que es un texto aleatorio que se combinara con nuestra password
            salt = gensalt()
            # Convertimos la password a bytes
            password = dataSerializada.get('password')
            passwordByes = password.encode('utf-8')

            passwordHashed = hashpw(passwordByes, salt).decode('utf-8')
            # reemplazamos nuestra password original por el hashing de la password
            dataSerializada['password'] = passwordHashed

            nuevoUsuario = UsuarioModel(**dataSerializada)

            conexion.session.add(nuevoUsuario)
            conexion.session.commit()

            encriptador = Fernet(environ.get('FERNET_KEY'))
            informacion = {
                "id": nuevoUsuario.id
            }
            # Encripta la informacion y me la retorna en bytes por lo que la tenemos que decodificar para que sea un string
            token = encriptador.encrypt(
                str(informacion).encode('utf-8')).decode('utf-8')

            enviarCorreoDeValidacion(nuevoUsuario.correo, token)

            resultado = self.serializer.dump(nuevoUsuario)

            return {
                'message': 'Usuario registrado exitosamente',
                'content': resultado
            }, 201

        except ValidationError as error:
            return {
                'message': 'Error al crear el usuario',
                'content': error.args
            }, 400


class HabilitarUsuario(Resource):
    serializer = HabilitarUsuarioSerializer()

    def post(self):
        data = request.get_json()
        print(data)
        try:
            dataValidada = self.serializer.load(data)
            token = dataValidada.get('token')

            encriptador = Fernet(environ.get('FERNET_KEY'))
            informacionSecreta = encriptador.decrypt(token).decode('utf-8')
            # convertimos un str a un dict
            informacionSecretaDict = literal_eval(informacionSecreta)
            print(informacionSecretaDict.get('id'))

            return {
                'message': 'Usuario habilitado exitosamente'
            }
        except ValidationError as error:
            return {
                'message': 'Error al obtener la token',
                'content': error.args
            }
