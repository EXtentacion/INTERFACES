#instanciamos la clase Flask
from flask import Flask,render_template,request

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
    return render_template('index.html')

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        Titulo = request.form['Titulo']
        Artista = request.form['Artista']
        Anio = request.form['Anio']
        print(Titulo)
        print(Artista)
        print(Anio)
        return 'Cambios guardados'
    
    

@app.route('/eliminar')
def eliminar():
    
    return 'Eliminar'





#creamos la ruta
if __name__ == '__main__':
    
    app.run(debug = True, port = 8000)



