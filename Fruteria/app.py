from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'DB_Floreria'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

@app.route('/')
def index1():
    CC = mysql.connection.cursor()
    CC.execute('SELECT * FROM tbflores')
    Flores = CC.fetchall()
    CC.close()
    return render_template('index.html', listaFlores=Flores)

@app.route('/buscar', methods=['POST'])
def buscar():
    if request.method == 'POST':
        nombre_buscar = request.form['txtBuscar']
        CC = mysql.connection.cursor()
        CC.execute("SELECT * FROM tbflores WHERE nombre LIKE %s", [nombre_buscar + '%'])
        Flores = CC.fetchall()
        CC.close()
        return render_template('index.html', listaFlores=Flores)

@app.route('/ingresar', methods=['POST'])
def ingresar():
    if request.method == 'POST':
        Vnombre = request.form['txtNombre']
        Vcantidad = request.form['Cantidad']
        Vprecio = request.form['Precio']
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO tbflores (nombre, cantidad, precio) VALUES (%s, %s, %s)', (Vnombre, Vcantidad, Vprecio))
        mysql.connection.commit()
        CS.close()
        
        flash('La flor fue agregada')
        return redirect(url_for('index1'))

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    CS = mysql.connection.cursor()
    CS.execute('SELECT * FROM tbflores WHERE id = %s', [id])
    flor = CS.fetchone()
    CS.close()

    if request.method == 'POST':
        Vnombre = request.form['txtNombre']
        Vcantidad = request.form['Cantidad']
        Vprecio = request.form['Precio']
        CS = mysql.connection.cursor()
        CS.execute("""
            UPDATE tbflores
            SET nombre = %s,
                cantidad = %s,
                precio = %s
            WHERE id = %s
        """, (Vnombre, Vcantidad, Vprecio, id))
        mysql.connection.commit()
        flash('La flor fue actualizada')
        return redirect(url_for('index1'))

    return render_template('editar.html', flor=flor)

@app.route('/eliminar/<id>', methods=['POST'])
def eliminar(id):
    if request.method == 'POST':
        CS = mysql.connection.cursor()
        CS.execute('DELETE FROM tbflores WHERE id = %s', [id])
        mysql.connection.commit()
        CS.close()
        
        flash('La flor fue eliminada')
        return redirect(url_for('index1'))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
