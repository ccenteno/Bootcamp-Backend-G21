from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import ProductoModel

class ProductoSerializer(SQLAlchemyAutoSchema):
    class Meta:
        # pasarle metadatos a la clase de la cual estamos heredando
        # model obtendrá toda l a configuracion del modelo y la pondra para cuestiones de serializador
        model = ProductoModel
        # para indicar al serializador que tambien haga la validacion de las columnas que son llaves  foraneas (FK) 
        include_fk = True
