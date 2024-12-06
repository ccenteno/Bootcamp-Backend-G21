from flask_restful import Resource, request
from models import ProductoModel
from marshmallow.exceptions import ValidationError
from .serializers import ProductoSerializer
from instancias import conexion

class ProductoController(Resource):
    def post(self):
        # Obtenemos la informacion del body proveniente del request
        data = request.get_json()
        serializador = ProductoSerializer()
        try:
            data_validada = serializador.load(data=data)
            # TODO: Antes de guardad el producto validar que exista la categoria, si es que el pasa, porque tambien puede haber productos sin categoria
            nuevo_producto = ProductoModel(**data_validada)

            conexion.session.add(nuevo_producto)
            conexion.session.commit()

            resultado = serializador.dump(nuevo_producto)
            return {'message': 'Producto creado exitosamente',
                    'content': resultado
                    }
        except ValidationError as error:
            return {'message': 'Error al crear el producto',
                    'content': error.args  # muestra la descripcion del error
                    }
