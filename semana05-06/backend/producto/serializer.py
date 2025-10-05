from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from .model import ProductoModel
from categoria.serializer import CategoriaSerializer


class ProductoSerializer(SQLAlchemyAutoSchema):
    # https://marshmallow.readthedocs.io/en/latest/marshmallow.fields.html#marshmallow.fields.Nested
    categoria = fields.Nested(
        nested=CategoriaSerializer, dump_only=True, only=('id', 'nombre'))

    class Meta:
        model = ProductoModel
        # hace que al momento de serializa/deserializar incluya las llaves foraneas que tenga este modelo
        include_fk = True
        # Hace que al momento de devolver la data se incluyan las relaciones pero las relaciones no son a nivel de base de datos sino a nivel del ORM
        # include_relationships = True
