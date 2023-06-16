#instanciamos la clase Flask
from flask import Flask

#inicializamos la app
app = Flask(__name__)
app.config ['MySQL_DATABASE_HOST'] = 'localhost'
app.config ['MySQL_DATABASE_USER'] = 'root'
app.config ['MySQL_DATABASE_PASSWORD'] = ''
app.config ['MySQL_DATABASE_DB'] = 'dbflask'






#Definimos la ruta  
@app.route('/')

#creamos la funcion
def index():
    return 'Hola mundo'

@app.route('/guardar')
def guardar():
    return 'Guardado'

@app.route('/eliminar')
def eliminar():
    
    return 'Eliminado'





#creamos la ruta
if __name__ == '__main__':
    
    app.run(debug = True, port = 8000)



