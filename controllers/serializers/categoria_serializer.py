from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import CategoriaModel

class CategoriaSerializer(SQLAlchemyAutoSchema):
    class Meta:
        # pasarle metadatos a la clase de la cual estamos heredando
        # model obtendrá toda l a configuracion del modelo y la pondra para cuestiones de serializador
        model = CategoriaModel

