from wsgiref.simple_server import make_server
import views


def app(environ, start_response):
    path = environ.get('PATH_INFO')
    if path == '/':
        return views.english_handle_index(environ, start_response)
    elif path == '/es/index.html':
        return views.page_index(environ, start_response)
    elif path == '/es/equipos.html':
        return views.page_index(environ, start_response)
    elif path == '/es/partidos.html':
        return views.page_index(environ, start_response)
    else:
        return views.handle_404(environ, start_response)


if __name__ == "__main__":
    host = 'localhost'
    port = 8000
    httpd = make_server(host, port, app)
    print(f"Servidor en http://{host}:{port}")
    httpd.serve_forever()
