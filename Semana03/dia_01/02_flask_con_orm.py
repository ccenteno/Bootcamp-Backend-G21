from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#generic-camelcase-types
from sqlalchemy import Column, types
from flask_migrate import Migrate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.exceptions import ValidationError


app = Flask(__name__)

# Aca agregamos la variable de conexion a nuestra base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://postgres:root@localhost:5432/bd_flask'

conexion = SQLAlchemy(app=app)

Migrate(app=app, db=conexion)

# Cada tabla que vayamos a crear sera como una clase
class ProductoModel(conexion.Model):
    # Herencia: Semana 1 Programacion Orientada a Objetos
    # ahora declaramos las columnas de la tabla como si fueran atributos de la clase

    # id ....serial primary key  > SQL
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    # nombre ... not null, > SQL
    nombre = Column(type_=types.Text, nullable=False)
    # precio ... not null > SQL
    precio = Column(type_=types.Float(precision=2), nullable=False)
    # serie ... not null unique > SQL
    serie = Column(type_=types.Text, nullable=False, unique=True)
    disponible = Column(type_=types.Boolean, nullable=True)
    #name > si queremos manejar un nombre en el backend y otro nombre en le bd con la propiedad name indicamos como se llamara en la tabla de la db.
    fechaVencimiento = Column(type_=types.Date, nullable=True, name='fecha_vencimiento')

    # para indicar comom queremos que se llame la tabla sin modificar el nombre de la clase
    __tablename__ = "productos"

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        # Sirve ára ásarle a la clase de la cual estamos heredando pero sin la necesidad de modficacar con tal la instancia de la clase
        model = ProductoModel
        # al indicar el modelo que se tiene que basar podra ubicar todos los atributos y ver sus restricciones (not null, unico, tipo de datos, etc)

# @app.route('/crear-tablas')
# def crear_tablas():
#     # creara todas las tablas que no esten en la base de datos
#     # si la tabla ya existe no la creara aun asi dentro de la tabla tenga modificaciones como agregar columna, quitar columna, relaciones, etc
#     # SIGUIENTE PASO: Usar migraciones
#     conexion.create_all()
#     return {
#         'message': 'Las tablas fueron creadas exitosamente'
#     }

@app.route('/productos', methods=['POST', 'GET'])
def gestion_productos():
    metodo = request.method
    if metodo=='POST':
        serializador = 
        # primero leeremos la informacion del cliente
        # convertimos el json a un diccionario para que Python lo procese
        data = request.get_json()
        try:
            serializador.load(data)
            nuevoProducto=ProductoModel(nombre=data.get('nombre'),
                                        precio=data.get('precio'),
                                        serie=data.get('serie'),
                                        disponible=data.get('disponible'),
                                        fechaVencimiento=data.get('fechaVencimiento'))
            #print(data)
            print('Producto antes de guardarse en la bd', nuevoProducto.id)
            #utilizamos la conexion para ir a la bd
            # empezamos una transaccion en la cual estamos indicando que agregaremos este registro
            conexion.session.add(nuevoProducto)

            # indicamos que los cambios tiene que guardarse de manera permanente
            conexion.sesion.commit()

            print('Producto luego de guardarse en la bd', nuevoProducto.id)
            return {
                'message': 'Registro creado exitosamente'
            }
        except ValidationError as error:
            # si falla al momento de hacer la validacion con el serializador
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            }
        except IntegrityError as error:
            # si falla al momento de guardar en la base de datos y el producto ya existe (nombre es unico)
            return {
                'message': 'Error al crear el producto',
                'content': 'El producto ya existe!'
            }
        
    elif metodo=='GET':
        # Establecemos una consulta de obtencion de datos
        # SELECT * FROM productos;
        productos = conexion.session.query(ProductoModel).all()
        # print(productos)
        # resultado=[]
        # for producto in productos:
        #     item={
        #         'id':producto.id,
        #         'nombre':producto.nombre,
        #         'precio':producto.precio,
        #         'serie':producto.serie,
        #         'disponible':producto.disponible,
        #         'fechaVencimiento':producto.fechaVencimiento
        #     }
        #     resultado.append(item)

        serializador = ProductSchema()
        # cuando convertimos la informacion desde la bd a un dict utilizamos el metodo dump
        # cuando pasamo un arreglo de instancias tenemos que agregar el parametro 
        resultado = serializador.dump(productos, many=True)

        return {'message':'Los productos son',
                'content':resultado
                }




if __name__ == "__main__":
   app.run(debug=True)
