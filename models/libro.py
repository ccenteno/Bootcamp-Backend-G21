from instancias import conexion
from sqlalchemy import Column, types, ForeignKey
from datetime import datetime

class Libro(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    titulo = Column(type_=types.Text, nullable=False)
    descripción = Column(type_=types.Text)
    cantidad = Column(type_=types.Integer)
    disponible = Column(type_=types.Boolean)
    fechaCreacion = Column(type_=types.TIMESTAMP, default=datetime.now) 
    categoriald = Column(ForeignKey(column='categorias.id'),
                         type_=types.Integer, nullable=False, 
                         name='categoria.id')
    
    __tablename__ = 'libros'

