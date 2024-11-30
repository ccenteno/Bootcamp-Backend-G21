from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError

class UsuarioSchema(Schema):
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    correo = fields.Email()
    sexo = fields.Str(required=True)

usuario1 = {'nombre': 'Ceesar',
            'apellido': 'Centeno',
            'correo': 'ccentenor@gamil.com'}

usuario2 = {'nombre': 'Rozana',
            'correo': 'rcccdse@gmail.com',
            'sexo': 'F'}

validarUsuario = UsuarioSchema()

# load > validará

try:
    resultado1 =validarUsuario.load(usuario1)

    print(resultado1)
except ValidationError as error:
    print(error.args)

try:
    resultado2 =validarUsuario.load(usuario2)
    print(resultado2)
except ValidationError as error:
    print(error.args)

# resultado2 =validarUsuario.load(usuario2)

class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo



print(resultado2)