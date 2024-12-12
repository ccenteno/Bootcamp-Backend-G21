from instancias import conexion
from sqlalchemy import Column, types
from enum import Enum

class TipoUsuario(Enum): 
    #la columna 
    ADMIN = 'ADMIN' 
    CLIENTE = 'CLIENTE' 
    EMPLEADO = 'EMPLEADO'

class Usuario(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text)
    apellido = Column(type_=types.Text)
    correo = Column(type_=types.String(100), unique=True, nullable=False)
    password = Column(type_=types.Text)
    tipoUsuario = Column(type_=types.Enum(TipoUsuario),
                         default = TipoUsuario.CLIENTE)
	
    __tablename__ = 'usuarios'

    # Si esta tabla sera creada y manejada en otra conexión que no es la predeterminada entonces usamos la variable bind_key para indicar que conexión debe usar
    __bind_key__ = 'mysql'
