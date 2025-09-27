from bd import conexion
from sqlalchemy import Column, types


class CategoriaModel(conexion.Model):
    # https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Column.__init__
    # https://docs.sqlalchemy.org/en/20/core/type_basics.html#
    id = Column(type_=types.Integer, autoincrement=True,
                nullable=False, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    orden = Column(type_=types.Integer, nullable=False)

    # Servira para poder modificar el nombre con el cual se creara la tabla en la bd
    __tablename__ = 'categorias'
