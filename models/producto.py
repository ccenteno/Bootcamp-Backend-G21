from instancias import conexion
from sqlalchemy import Column, types, ForeignKey
from datetime import datetime
# ProductoModel
# id Integer, pk, autoincrementable
# nombre Text no puede ser null
# descripcion Text puede ser null
# precio Float y no puede ser null
# disponibilidad Boolean y su valor por defecto va a ser True

# nombre de la tabla sea 'productos'
# ademas agregar el bind_key

class ProductoModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True,
                primary_key=True, nullable=False)
    nombre = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_=types.Text, nullable=True)
    precio = Column(type_=types.Float, nullable=False)
    fechaCreacion = Column(name='fecha_creacion',type_=types.TIMESTAMP, default=datetime.now)
    disponibilidad = Column(type_=types.Boolean, default=True)

    # Relaciones
    # En este caso estariamos utilizando una relacion de 1 a n
    categoriaId = Column(ForeignKey(column='categorias.id'),
                         type_=types.Integer,nullable=False)

    __tablename__ = 'productos'
    # si en nuestra instancia de sqlalchemy estamos usando mas de un conector, entonces debemos en cada tabla que usemos, indicar a que conexion nos referimos, esto servira para cuestiones de creacion de tabla y para la lectura y modificacion de datos
    __bind_key__ = 'postgres'
