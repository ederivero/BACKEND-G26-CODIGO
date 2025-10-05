from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .model import ProductoModel


class ProductoSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = ProductoModel
        # hace que al momento de serializa/deserializar incluya las llaves foraneas que tenga este modelo
        include_fk = True
