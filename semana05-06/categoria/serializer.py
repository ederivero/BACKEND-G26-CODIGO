from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .model import CategoriaModel


class CategoriaSerializer(SQLAlchemyAutoSchema):
    class Meta:
        # Modificar los atributos de la clase que estamos heredando sin la necesidad de crear un metodo para editarlos, sino que directamente se hace dentro de la clase Meta (Metadata)
        model = CategoriaModel
