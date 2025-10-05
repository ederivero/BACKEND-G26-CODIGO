from bd import conexion
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship


class ProductoModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    precio = Column(type_=types.Float, nullable=False)
    descripcion = Column(type_=types.Text)
    disponible = Column(type_=types.Boolean, default=True)

    # Relaciones
    categoriaId = Column(ForeignKey(column='categorias.id'),
                         nullable=True, name='categoria_id')

    # Relationships
    # es la relacion pero a nivel del ORM , esto no afecta en nada a la bd, podemos crear relationships sin la necesidad de tener nuestras relaciones en la bd
    categoria = relationship('CategoriaModel')

    __tablename__ = 'productos'
