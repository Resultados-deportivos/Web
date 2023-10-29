import psycopg2

# Database connection parameters
db_connection = {
    "database": "eusko_basket",
    "user": "admin_basket",
    "password": "Reto@123",
    "host": "pgsql03.dinaserver.com",
    "port": "5432",
}

# Create a connection to the database
conn = psycopg2.connect(
    database=db_connection["database"],
    user=db_connection["user"],
    password=db_connection["password"],
    host=db_connection["host"],
    port=db_connection["port"],
)

# Create a cursor
cur = conn.cursor()
cur2 = conn.cursor()

# Define a class to represent Publicacion objects
class Publicacion:
    def __init__(self, id, img, titulo, descripcion):
        self.id = id
        self.img = img
        self.titulo = titulo
        self.descripcion = descripcion

class Usuario:
    def __init__(self, id, nombre, contrasena, correo, admin):
        self.id = id
        self.nombre = nombre
        self.contrasena = contrasena
        self.correo = correo
        self.admin = admin


# Execute a SQL query to fetch Publicacion records
cur.execute("SELECT * FROM publicaciones")
cur2.execute("SELECT * FROM usuarios")

# Fetch all results and map them to Publicacion objects
results = []
for row in cur.fetchall():
    Id, img, titulo, descripcion = row
    publicacion = Publicacion(id, img, titulo, descripcion)
    results.append(publicacion)

results_users = []
for row in cur2.fetchall():
    Id, nombre, correo, contrasena, admin = row
    users = Usuario(id, nombre, correo, contrasena, admin)
    results_users.append(users)

# Close the cursor and connection
cur.close()
cur2.close()
conn.close()
if __name__ == '__main__':
    # Print the results
    for publicacion in results:
        print(
            f"ID: {publicacion.id}, Img: {publicacion.img}, Titulo: {publicacion.titulo}, Descripcion: {publicacion.descripcion}")
    for users in results_users:
        print(
            f"ID: {users.id}, Nombre: {users.nombre}, Correo: {users.correo}, Contrasena: {users.contrasena}, Admin: {users.admin}")
