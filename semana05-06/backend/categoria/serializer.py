from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import Schema, fields
from .model import CategoriaModel


class CategoriaSerializer(SQLAlchemyAutoSchema):
    # auto_field > permite editar alguna columna (Atributo) que esta en el modelo
    # dump_only > solo usaremos este campo para cuando mostremos la informacion mas no para cuando la validemos (load)
    posicion = auto_field(dump_only=True)

    class Meta:
        # Modificar los atributos de la clase que estamos heredando sin la necesidad de crear un metodo para editarlos, sino que directamente se hace dentro de la clase Meta (Metadata)
        model = CategoriaModel


class ReordenarCategoriaSerializer(Schema):
    categoriaId = fields.Int(required=True)
    idVecinoAnterior = fields.Int(required=False)
    idVecinoProximo = fields.Int(required=False)
