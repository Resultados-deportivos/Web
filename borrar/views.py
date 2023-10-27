from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('./templates/'))
template = env.get_template('index.html')

# Funciones para manejar las rutas específicas
def english_handle_index(environ, start_response):
    # Lógica para la ruta '/en'
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [b'Hello, English World!']

def spanish_handle_index(environ, start_response):
    # Lógica para la ruta '/es'
    tareas = ['tarea 1', 'tarea2']
    response = template.render(tasks=tareas).encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    # return [b'Hola, Mundo en Espanol!']
    return [response]

def handle_404(environ, start_response):
    # Lógica para manejar una ruta no reconocida (404)
    status = '404 Not Found'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [b'Pagina no encontrada']