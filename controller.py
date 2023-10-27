from wsgiref.simple_server import make_server
import views
from views import page_index, page_equipos, page_competiciones, page_partidos, serve_static, serve_static_img


def app(environ, start_response):
    path = environ.get('PATH_INFO')
    if path == '/es/index.html':
        return page_index(environ, start_response)
    elif path == '/es/competiciones.html':
        return page_competiciones(environ, start_response)
    elif path == '/es/equipos.html':
        return page_equipos(environ, start_response)
    elif path == '/es/partidos.html':
        return page_partidos(environ, start_response)
    elif path == '/static/style.css':
        # Serve the "style.css" file from the static folder
        return serve_static(environ, start_response, path)
    elif path.startswith('/static/img/'):
        # Serve images from the "img" subfolder in the static directory
        return serve_static_img(environ, start_response, path)
    else:
        return views.handle_404(environ, start_response)


if __name__ == "__main__":
    host = 'localhost'
    port = 8000
    httpd = make_server(host, port, app)
    print(f"Servidor en http://{host}:{port}")
    httpd.serve_forever()
