from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .model import Usuario


class RegistrarUsuario(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
