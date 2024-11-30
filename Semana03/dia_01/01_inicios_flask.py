from flask import Flask, request
from psycopg import connect
# __name__ > propia de python que sirve para indicar si el archivo en el cual nos encontramos es el archivo principal (el que se esta ejecutando por la terminal). si es el archivo principal su valor sera '__main__', caso contrario tendra otro valor la variable
app = Flask(__name__)
# Flask solamente puede tener una instancia en todo el proyecto y esa instancia debe de estar en el archivo principal, sino no podra ejecutarse la instancia de la clase

conexion = connect(
    conninfo='postgresql://postgres:ccenteno@localhost:5432/finanzas')

# Mediante el uso de decoradores podemos indicar la ruta y cual será su comportamiento
@app.route('/')
def inicio():
   return 'Bienvenido a mi aplicacion de Flask'

@app.route('/inicio', methods=['POST'])
def inicio_aplicacion():
   return {'mensaje':'Buenas noches, acabas de descubrir otro endpoint'}

# Si queremos un parametro por la url que sea dinamico, este parametro tiene que estar entro < >, adicional a ello se puede indicar el tipo de dato (int, string)
@app.route('/usuarios/<int:id>', methods=['GET','POST'])
def mostrar_usuario(id):
   # cuando ponemos un parametro dinamico entonces ese parametro tiene que ser registrado con el mismo nombre como parametro de la funcion
   print(id)
   # return {'mensaje': 'El usuario es '+str(id)}
   return {'mensaje': f'El usuario es {id}'}

@app.route('/gestionar-usuario/<int:id>',methods=['POST','PUT','DELETE'])
def gestionar_usuario(id):
   if request.method=='POST':
      return {'mensaje': 'La creacion del usuario fue exitosa'}
   elif request.method=='PUT':
      return {'mensaje': 'Usuario actualizado exitosamente'}
   elif request.method=='DELETE':
      return {'mensaje': 'Usuario eliminado exitosamente'}

@app.route('/listar-clientes', methods=['GET'])
def listar_clientes():
   cursor = conexion.cursor()
   cursor.execute("SELECT * FROM CLIENTES")

   data = cursor.fetchall()
   lista=[]
   for dato in data:
      # fila = f"'id':{dato[0]},'nombre':'{dato[1]}','correo':'{dato[2]}'"
      fila = {'id':dato[0], 'nombre':dato[1], 'correo':dato[2], 'status':dato[3],'activo':dato[4],'fechaCreacion':dato[5]}
      lista.append(fila)
   print(lista)
   return {'mensaje': 'Los clientes son',
           'content': lista}

# @app.route('/cliente/<int:id>', methods=['GET'])
# def cliente(id):
#    cursor = conexion.cursor()
#    cursor.execute(f"SELECT * FROM CLIENTES WHERE ID={id}")
# 
#    data = cursor.fetchall()
#    lista=[]
#    for dato in data:
#       fila = {'id':dato[0],'nombre':dato[1],'correo':dato[2],'status':dato[3],'activo':dato[4],'fechaCreacion':dato[5]}
#       lista.append(fila)
#    print(lista)
#    return {'mensaje': f'El ciente con id {id}',
#            'content': lista}

@app.route('/cliente/<int:id>', methods=['GET'])
def cliente(id):
   cursor = conexion.cursor()
   cursor.execute(f"SELECT * FROM CLIENTES WHERE ID={id}")
   
   dato = cursor.fetchone()
   lista=[]
   print(dato)
   if dato != '' :
      fila = {'id':dato[0],'nombre':dato[1],'correo':dato[2],'status':dato[3],'activo':dato[4],'fechaCreacion':dato[5]}
      lista.append(fila)
   print(lista)
   return {'mensaje': f'El ciente con id {id}',
           'content': lista}

# Toda la funcionalidad de nuestro servidor tiene que antes del método .run
# levanta el servidor de Flask con algunos parametros opcionales
# debug > si su valor es True entonces cada vez que modifiquemos el servidor y guardemos este se reiniciara automaticamente
app.run(debug=True)
