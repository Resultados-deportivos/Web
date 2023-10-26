import psycopg2
from flask import Flask, render_template, redirect, url_for
import modelos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

db_connection = {
    "database": "eusko_basket",
    "user": "admin_basket",
    "password": "Dinahosting2209@",
    "host": "pgsql03.dinaserver.com",
    "port": "5432"
}

engine = create_engine(
    f'postgresql://{db_connection["user"]}:{db_connection["password"]}@{db_connection["host"]}:{db_connection["port"]}/{db_connection["database"]}'
)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Index (Redirecciones)
@app.route('/es/index.html')
def home():
    jugadores = session.query(modelos.Jugador).all()
    print(jugadores)
    return render_template('index.html' )


@app.route('/es/')
def index_es():
    return redirect(url_for('home'))


@app.route('/')
def index():
    return redirect(url_for('home'))


# Equipos.hmtl
@app.route('/es/equipos.html')
def page_equipos():
    return render_template('equipos.html')


@app.route('/es/competiciones.html')
# Competiciones.html
def page_compe():
    return render_template('competiciones.html')


@app.route('/es/partidos.html')
# Partidos.html
def page_partidos():
    return render_template('partidos.html')


# Error Page
@app.route('/404')
def page_not_found():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
