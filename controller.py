from wsgiref.simple_server import make_server
import views
from views import page_index, page_equipos, page_competiciones, page_partidos, page_login, serve_static, serve_static_img, serve_static_js


def app(environ, start_response):
    path = environ.get('PATH_INFO')
    # Inicio
    if path == '/es/inicio':
        return page_index(environ, start_response)
    # Competiciones
    elif path == '/es/competiciones':
        return page_competiciones(environ, start_response)
    # Equipos
    elif path == '/es/equipos':
        return page_equipos(environ, start_response)
    # Partidos
    elif path == '/es/partidos':
        return page_partidos(environ, start_response)
    elif path == '/es/sign-in':
        return page_login(environ, start_response)
    elif path == '/es/sign-up':
        return page_login(environ, start_response)
    # Load CSS
    elif path == '/static/style.css':
        # Serve the "style.css" file from the static folder
        return serve_static(environ, start_response, path)
    # Load Folder /static/Img
    elif path.startswith('/static/img/'):
        # Serve images from the "img" subfolder in the static directory
        return serve_static_img(environ, start_response, path)
    # Load JS Do not work
    elif path.startswith('/static/script.js'):
        # Serve images from the "img" subfolder in the static directory
        return serve_static_js(environ, start_response, path)
    # Do not found
    else:
        return views.handle_404(environ, start_response)


if __name__ == "__main__":
    host = 'localhost'
    port = 8000
    httpd = make_server(host, port, app)
    print(f"Servidor en http://{host}:{port}")
    httpd.serve_forever()
