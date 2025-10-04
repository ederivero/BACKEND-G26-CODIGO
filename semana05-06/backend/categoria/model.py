from bd import conexion
from sqlalchemy import Column, types


class CategoriaModel(conexion.Model):
    # https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Column.__init__
    # https://docs.sqlalchemy.org/en/20/core/type_basics.html#
    id = Column(type_=types.Integer, autoincrement=True,
                nullable=False, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    posicion = Column(type_=types.Float, nullable=False)
    # fecha > deletedAt (la fecha de cuando se "elimino")
    # deleted > boolean
    deletedAt = Column(type_=types.DateTime, name='deleted_at')

    # Servira para poder modificar el nombre con el cual se creara la tabla en la bd
    __tablename__ = 'categorias'
