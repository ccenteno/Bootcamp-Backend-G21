from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#generic-camelcase-types
from sqlalchemy import Column, types

app = Flask(__name__)

# Aca agregamos la variable de conexion a nuestra base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://postgres:root@localhost:5432/bd_flask'

conexion = SQLAlchemy(app=app)


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
        # primero leeremos la informacion del cliente
        # convertimos el json a un diccionario para que Python lo procese
        data = request.get_json()
        nuevoProducto=ProductoModel(nombre=data.get('nombre'),
                                    precio=data.get('precio'),
                                    serie=data.get('serie'),
                                    disponible=data.get('disponible'),
                                    fechaVencimiento=data.get('fechaVencimiento'))
        #print(data)
        print('Producto antes de guardarse en la bd', nuevoProducto.id)
        #utilizamos la conexion para ir a la bd
        conexion.session.add(nuevoProducto)

        conexion.sesion.commit()

        print('Producto luego de guardarse en la bd', nuevoProducto.id)
        return {
            'message': 'Registro creado exitosamente'
        }
    elif metodo=='GET':
        productos = conexion.session.query(ProductoModel).all()

        print(productos)
        return {'message':'Los productos son',
                }




if __name__ == "__main__":
   app.run(debug=True)
