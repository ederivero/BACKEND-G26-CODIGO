from flask_restful import Resource, Api, request
from flask import Blueprint
from .model import CategoriaModel
from bd import conexion
from .serializer import CategoriaSerializer
from marshmallow.exceptions import ValidationError

# Ahora registraremos nuestro blueprint (mini aplicacion de categorias)
categorias_blueprint = Blueprint('categorias_bp', __name__)

# Con la clase Api nosotros declaramos los recursos de los controladores como los recursos a ser consumidos en nuestra aplicacion de flask
categoria_api = Api(categorias_blueprint)


# Al momento de heredar la clase Resource ahora los metodos http que declaremos como metodos de la clase serviran para poderlos consumir como metodos http
class Categorias(Resource):
    # Este sera un atributo que podra ser usado en todos los metodos de mi clase
    serializador = CategoriaSerializer()

    def get(self):
        # Asi se utiliza el ORM
        # SELECT * FROM categorias;
        categorias = conexion.session.query(CategoriaModel).all()

        resultado = self.serializador.dump(categorias, many=True)

        return {
            'message': 'Las categorias son',
            'content': resultado
        }

    def post(self):
        body = request.get_json()
        try:
            # { "nombre": "Entradas", "orden": 2 }
            dataSerializada = self.serializador.load(body)
            # CategoriaModel(nombre=dataSerializada.get('nombre'),
            #                orden=dataSerializada.get('orden'))

            # ** en paso de parametros lo que hace es convierte el diccionario a sus llaves las vuelve los parametros y sus valores a los valores de esos parametros
            nuevaCategoria = CategoriaModel(**dataSerializada)
            # Añadimos a la conexion nuestra nueva categoria
            conexion.session.add(nuevaCategoria)
            # Guardamos de manera permanente nuestra nueva categoria en la bd
            conexion.session.commit()
            # dump agarra la instancia del registro y lo convierte a un diccionario
            resultado = self.serializador.dump(nuevaCategoria)

            return {
                'message': 'Categoria creada exitosamente',
                'content': resultado
            }, 201
        except ValidationError as error:
            return {
                'message': 'Error al crear la categoria',
                'content': error.args
            }


# /categoria/:id
class Categoria(Resource):
    serializador = CategoriaSerializer()

    def get(self, id):
        # SELECT * FROM categorias WHERE id = '' LIMIT 1;
        categoriaEncontrada = conexion.session.query(
            CategoriaModel).filter(CategoriaModel.id == id).first()

        if not categoriaEncontrada:
            return {
                'message': 'La categoria no existe'
            }, 404  # not found

        result = self.serializador.dump(categoriaEncontrada)

        return {
            'content': result
        }, 200  # ok (por defecto si no se le pone nada)


# Luego de haber declarado todos nuestros Recursos ahora agregaremos esos recursos a nuestra Api
categoria_api.add_resource(Categorias, '/categorias')
