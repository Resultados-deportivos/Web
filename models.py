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

# Define a class to represent Publicacion objects
class Publicacion:
    def __init__(self, id, img, titulo, descripcion):
        self.id = id
        self.img = img
        self.titulo = titulo
        self.descripcion = descripcion

# Execute a SQL query to fetch Publicacion records
cur.execute("SELECT * FROM publicaciones")

# Fetch all results and map them to Publicacion objects
results = []
for row in cur.fetchall():
    id, img, titulo, descripcion = row
    publicacion = Publicacion(id, img, titulo, descripcion)
    results.append(publicacion)

# Close the cursor and connection
cur.close()
conn.close()

# Print the results
for publicacion in results:
    print(f"ID: {publicacion.id}, Img: {publicacion.img}, Titulo: {publicacion.titulo}, Descripcion: {publicacion.descripcion}")
