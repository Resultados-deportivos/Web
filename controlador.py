import jinja2

def render_template(template_name, **context):
    template_loader = jinja2.FileSystemLoader(searchpath="templates")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(template_name)
    return template.render(**context)

def home():
    # Lógica para obtener datos del modelo (si es necesario)
    # Por ejemplo, data = obtener_datos_del_modelo()

    # Renderiza la plantilla y pasa los datos
    return render_template('index.html')

def page_equipos():
    # Lógica para obtener datos del modelo (si es necesario)
    # Por ejemplo, data = obtener_datos_del_modelo()

    # Renderiza la plantilla y pasa los datos
    return render_template('equipos.html')

# Define otras funciones de controlador para las otras páginas


