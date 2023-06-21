#instanciamos la clase Flask
from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL

#inicializamos la app
app = Flask(__name__)
app.config ['MySQL_HOST'] = 'localhost'
app.config ['MySQL_USER'] = 'six'
app.config ['MySQL_PASSWORD'] = ''
app.config ['MySQL_DB'] = 'dbflask'


mysql = MySQL(app)


#CREATE TABLE albums (id INT(11) AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(255), artista VARCHAR(255), anio INT(11));


     

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
        cur= mysql.connection.cursor()
        cur.execute('INSERT INTO albums (titulo,artista,anio) VALUES (%s,%s,%s)',(Titulo,Artista,Anio))
        mysql.connection.commit()
        return 'Recibido'
    return redirect(url_for('index'))

    
    

@app.route('/eliminar')
def eliminar():
    
    return 'Eliminar'





#creamos la ruta
if __name__ == '__main__':
    
    app.run(debug = True, port = 8000)



