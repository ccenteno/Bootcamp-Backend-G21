from instancias import conexion
from sqlalchemy import Column, types

class PruebaModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text)

    __tablename__ = 'pruebas'
    # si en nuestra instancia de sqlalchemy estamos usando mas de un conector, entonces debemos en cada tabla que usemos, indicar a que conexion nos referimos, esto servira para cuestiones de creacion de tabla y para la lectura y modificacion de datos
    #__bind_key__ = 'postgres2'