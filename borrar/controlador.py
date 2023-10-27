from wsgiref.simple_server import make_server
import views

# Define la función app que manejará las solicitudes.
def app(environ, start_response):
    path = environ.get('PATH_INFO')
    if path == '/':
        return views.english_handle_index(environ, start_response)
    elif path == '/es':
        return views.spanish_handle_index(environ, start_response)
    else:
        return views.handle_404(environ, start_response)



if __name__ == "__main__":
    host = 'localhost'
    port = 8000

    httpd = make_server(host, port, app)
    print(f"Servidor en http://{host}:{port}")
    httpd.serve_forever()
'''
Una vez ejecutado el controlador, podemos acceder a través del navegador, 
con las rutas: http://localhost:8000/    (no se usa jinja2)
y   http://localhost:8000/es, esta segunda usa jinja2.
Si se pone una url diferente, saldrá el mensaje de 'página no encontrada'
'''