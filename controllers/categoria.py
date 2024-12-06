from flask_restful import Resource, request
from models import CategoriaModel
from instancias import conexion
from .serializers import CategoriaSerializer
from marshmallow.exceptions import ValidationError

# Al heredar la casa Resource, ahora los modulos tendran que tener el nombre de los metodos http para que sean llamados correctamente

class CategoriaController(Resource):
    def get(self):
        # SELECT * FROM categorias;
        data = conexion.session.query(CategoriaModel).all()
        # convertir esta informacion de instancias a un diccionario para devolverlo usandp marshmallow
        serializador = CategoriaSerializer()
        resultado = serializador.dump(data, many=True)
        return {
            'message': 'Las categorias son',
            'result': resultado
        }
    
    def post(self):
        # Obtenemos la informacion del body proveniente del request
        data = request.get_json()
        serializador = CategoriaSerializer()
        try:
            # carga la informacion y la validara con el serializador, si falla, emitira un error
            data_serializada = serializador.load(data=data)

            # Cargo la infromacion serializa a la nueva instancia de la categoria
            # CategoriaModel(nombre=data_serializada.get('nombre'),
            #                fechaCreacion=data_serializada.get('fechaCreacion'), ...)

            # Cuando yo quiero pasar un diccionario de una clase o funcion CON LOS MISMOS NOMBRES
            # de los parametros que la llaves del diccionario
            # data_serializada = {'nombre': 'xyz', 'fechaCreacion': '2022-12-01'}
            # CategoriaModel('nombre': 'xyz', 'fechaCreacion': '2022-12-01')
            nueva_categoria = CategoriaModel(**data_serializada)
            
            # Agregamos el nuevo registro a la bd
            conexion.session.add(nueva_categoria)

            # Indicamos que los cambios deben de guardarse de manera permanente (usando transaccion)
            conexion.session.commit

            # Ahora convertimos la instancia a un diccionario para devolverla
            resultado = serializador.dump(nueva_categoria)
            return {'message': 'Categoria creada exitosamente',
                    'content': resultado
                    }
        except ValidationError as error:
            return {'message': 'Error al crear categoria',
                    'content': error.args  # muestra la descripcion del error
                    }

# cuando queremos trabajar en otra ruta o utilizar otra vez  un metodo ya creado
# Cuando ponemos en un metodo http un parametro que significa que vamos a recibir ese parametro por la url
# /endpoint/<id>    
class ManejoCategoriaController(Resource):
    def validarCategoria(self, id):
        # filter > hace la comparacion entre los atributos de la clase
        # filter_by > hace la comparacion entre PARAMETROS mas no utiliza atributos, SOLO SIRVE PARA HACER BUSQUEDAS IGUAL QUE
        # el filter es mejor porque nos permite hacer busquedas mas avanzadas como LIKE, ILIKE, mayor que, etc

        # SELECT * FROM categorias WHERE id = '...' LIMIT = 1;
        categoria_encontrada=conexion.session.query(CategoriaModel).filter(
            CategoriaModel.id == int(id)).first()

        if categoria_encontrada is None:
            return {'message': 'Categoria no existe'}
        return categoria_encontrada
    
    def get(self, id):

        categoria_encontrada = self.validarCategoria(id)

        serializador = CategoriaSerializer()
        resultado = serializador.dump(categoria_encontrada)

        return {'content': resultado}