from flask_restful import Api, request, Resource


class RegistrarUsuario(Resource):
    def post(self):
        data = request.get_json()

        return {
            'message': 'Usuario registrado exitosamente'
        }, 201
