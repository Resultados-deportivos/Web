import http.server
import socketserver
from http import HTTPStatus
from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment and specify the templates directory
env = Environment(loader=FileSystemLoader("templates"))

# Define the request handler
class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/static/'):
            # Serve static files directly from the "static" directory
            super().do_GET()
        else:
            # Create a dictionary for dynamic data
            data = {
                "title": "My Web Page",
                "content": "This is the content of the page.",
            }
            # Define the template to use
            template_name = ""

            if self.path == '/es/index.html':
                template_name = "index.html"
            elif self.path == '/es/equipos.html':
                template_name = "equipos.html"
            elif self.path == '/es/competiciones.html':
                template_name = "competiciones.html"
            elif self.path == '/es/partidos.html':
                template_name = "partidos.html"
            elif self.path == '/404':
                template_name = "error.html"

            if template_name:
                # Load the template by name (without the .html extension)
                template = env.get_template(template_name)
                # Render the template with the data
                response = template.render(data)
                self.send_response(HTTPStatus.OK)
                self.end_headers()
                self.wfile.write(response.encode('utf-8'))
            else:
                self.send_response(HTTPStatus.NOT_FOUND)
                self.end_headers()
                self.wfile.write("Page not found.".encode('utf-8'))

# Create a server and bind it to a port
with socketserver.TCPServer(("", 8000), CustomRequestHandler) as httpd:
    print("Serving at port 8000")
    httpd.serve_forever()
