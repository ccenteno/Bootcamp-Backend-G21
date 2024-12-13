from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models import Usuario, TipoUsuario
from marshmallow_enum import EnumField

class RegistroSerializer(SQLAlchemyAutoSchema):
    # si quiero modificar alguna columna del modelo para cuestiones del serializador
    # ahora modificamos la columna password y le indicamos que tiene que ser requerida a la hora de serializar
    password = auto_field(required=True)
    # modificar el comportamiento de la columna que sea enum en la cual se le coloca que enum debe utilizar para hacer las validaciones correspondientes

    tipoUsuario = EnumField(TipoUsuario)

    class Meta:
        model = Usuario
