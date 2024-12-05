# si queremos utilizar una carpeta como un conjunto de archivos que podremos utilizar en nuestro proyecto lo que podemos hacer es crear el archivo __init__.py para que podamos exportar todas las funcionalidades en este archvo y se puedan importar de una manera mas facil en otras partes 
from .categoria import CategoriaModel
from .producto import ProductoModel
from .prueba import PruebaModel

