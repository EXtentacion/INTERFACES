from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Función para establecer la conexión con la base de datos SQLite
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ruta principal
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM albums')
    albums = cur.fetchall()
    conn.close()
    return render_template('index.html', listAlbums=albums)

# Ruta para guardar un nuevo álbum
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo = request.form.get('txtTitulo')
        artista = request.form.get('txtArtista')
        año = request.form.get('txtAño')

        if titulo and artista and año:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO albums (Titulo, Artista, Año) VALUES (?, ?, ?)', (titulo, artista, año))
            conn.commit()
            conn.close()
            flash('Album Agregado Correctamente bro')
        else:
            flash('Todos los campos son requeridos')

    return redirect(url_for('index'))


# Ruta para editar un álbum
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM albums WHERE ID = ?', (id,))
    album = cur.fetchone()

    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        año = request.form['txtAño']
        cur.execute('UPDATE albums SET Titulo = ?, Artista = ?, Año = ? WHERE ID = ?', (titulo, artista, año, id))
        conn.commit()
        conn.close()
        flash('Album Modificado Correctamente bro')
        return redirect(url_for('index'))

    conn.close()
    return render_template('EditarAlbum.html', album=album)

# Ruta para eliminar un álbum
@app.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM albums WHERE ID = ?', (id,))
    conn.commit()
    conn.close()
    flash('Album Eliminado Correctamente bro')
    return redirect(url_for('index'))

# Crear la tabla "albums" si no existe
def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS albums (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Titulo TEXT NOT NULL,
            Artista TEXT NOT NULL,
            Año TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Ejecutar la función para crear la tabla
create_table()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
