from flask import Flask, render_template, Flask, redirect, url_for
import psycopg2

app = Flask(__name__, static_url_path='/static')


# Configurar la conexión a la base de datos PostgreSQL
#conn = psycopg2.connect(
   # database="mydb",
  #  user="miusuario",
 #   host="localhost"
#)

# Ruta principal (Redirecciones)
@app.route('/es/index.html')
def home():
    # Realizar una consulta SQL a la base de datos
    #cursor = conn.cursor()
    #cursor.execute("SELECT * FROM tu_tabla")
    #resultados = cursor.fetchall()
    #cursor.close()
#    return render_template('index.html', resultados=resultados)
    return render_template('index.html')
@app.route('/es/')
def index_es():
    return redirect(url_for('home'))
@app.route('/')
def index():
    return redirect(url_for('home'))
@app.route('/es/equipos.html')
def page_equipos():
    return render_template('equipos.html')
@app.route('/es/competiciones.html')
def page_compe():
    return render_template('competiciones.html')
@app.route('/es/partidos.html')
def page_partidos():
    return render_template('partidos.html')
# Error Page
@app.route('/404')
def page_not_found():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)