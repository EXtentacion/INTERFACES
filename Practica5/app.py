from flask import Flask, redirect, render_template, request, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'mysecretkey'

# MySQL configuration
mysql_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'datos',
    'port': '3307'
}

def fetch_data_from_mysql():
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**mysql_config)
        
        # Execute a query to fetch data from the database
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM albums")
        
        # Fetch all the data from the query
        data = cursor.fetchall()
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
        
        return data

    except mysql.connector.Error as err:
        print("Error accessing MySQL: ", err)
        return None

@app.route('/')
def index():
    # Fetch data from MySQL
    data_from_mysql = fetch_data_from_mysql()

    return render_template('index.html', listAlbums=data_from_mysql)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method =='POST':
        #pasamos a variables el contenido de los inputs
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
        
        try:
            # Establish a connection to the MySQL database
            connection = mysql.connector.connect(**mysql_config)
            
            # Execute the insert query
            cursor = connection.cursor()
            cursor.execute('INSERT INTO albums(titulo, artista, anio) VALUES (%s, %s, %s)', (Vtitulo, Vartista, Vanio))
            
            # Commit the changes
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()
            
            # Mensaje de éxito usando flash
            flash('El álbum fue agregado correctamente', 'success')
            
        except mysql.connector.Error as err:
            print("Error accessing MySQL: ", err)
            flash('Error al agregar el álbum', 'danger')

    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**mysql_config)
        
        # Execute a query to fetch data from the database
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM albums WHERE id=%s', (id,))
        
        # Fetch the data from the query
        constID = cursor.fetchone()
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
        
    except mysql.connector.Error as err:
        print("Error accessing MySQL: ", err)
        constID = None

    return render_template('editarAlbum.html', album=constID)

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        # Recuperar los datos editados del formulario
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']

        try:
            # Establecer conexión con la base de datos MySQL
            connection = mysql.connector.connect(**mysql_config)

            # Ejecutar la consulta para actualizar los datos del álbum
            cursor = connection.cursor()
            cursor.execute('UPDATE albums SET titulo=%s, artista=%s, anio=%s WHERE id=%s', (Vtitulo, Vartista, Vanio, id))

            # Confirmar los cambios
            connection.commit()

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()

            # Mensaje de éxito usando flash
            flash('El álbum fue actualizado correctamente', 'success')

        except mysql.connector.Error as err:
            print("Error al acceder a MySQL: ", err)
            flash('Error al actualizar el álbum', 'danger')

    return redirect(url_for('index'))

@app.route('/borrar/<int:id>')
def borrar(id):
    try:
        # Establecer conexión con la base de datos MySQL
        connection = mysql.connector.connect(**mysql_config)

        # Ejecutar la consulta para borrar el álbum
        cursor = connection.cursor()
        cursor.execute('DELETE FROM albums WHERE id=%s', (id,))

        # Confirmar los cambios
        connection.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        # Mensaje de éxito usando flash
        flash('El álbum fue borrado correctamente', 'success')

    except mysql.connector.Error as err:
        print("Error al acceder a MySQL: ", err)
        flash('Error al borrar el álbum', 'danger')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
