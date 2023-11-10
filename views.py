from jinja2 import Environment, FileSystemLoader
from models import *
from flash_manager import *
from utilities import *
from http import cookies
import datetime
import time


env = Environment(loader=FileSystemLoader('templates'))
index = env.get_template('index.html')
publicacion = env.get_template('publicacion.html')
competiciones = env.get_template('competiciones.html')
equipos = env.get_template('equipos.html')
partidos = env.get_template('eventos.html')
error = env.get_template('error.html')
sign_in = env.get_template('sign-in.html')
sign_up = env.get_template('sign-up.html')
admin = env.get_template('admin.html')
crud = env.get_template('crud.html')
forgot_pass = env.get_template('forgot_password.html')
forgot_pass_code = env.get_template('forgot_passwd_code.html')
set_new_pass = env.get_template('set_new_password.html')
logout = env.get_template('logout.html')
user_info = {}


def page_index(environ, start_response):
    global user_info

    if environ['REQUEST_METHOD'] == 'POST':
        form_data = parse_post_data(environ)
        comment = form_data.get('comment')
        publication_id = form_data.get('publication_id')
        publication_id = int(publication_id[0])
        print(user_info)
        print(comment, publication_id)
        print(user_info['id'])

        insert_coments_data(user_id=user_info['id'], publication_id=publication_id, description=str(comment[0]))
    publicaciones = get_posts()
    comments_list = get_comments()
    response = index.render(user_info=user_info, publicaciones=publicaciones, comments_list=comments_list, css_name='inicio.css').encode(
        'utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]


def page_publicacion(environ, start_response):
    global user_info

    if environ['REQUEST_METHOD'] == 'POST':
        form_data = parse_post_data(environ)
        comment = form_data.get('comment')
        publication_id = form_data.get('publication_id')
        publication_id = int(publication_id[0])
        # print(user_info)
        # print(comment, publication_id)
        # print(user_info['id'])

        # Check if the user is logged in
        if user_info:
            # Check if the like or dislike button is clicked
            if 'like-button' in form_data:
                handle_like_action(publication_id, user_info['id'])
            elif 'dislike-button' in form_data:
                handle_dislike_action(publication_id, user_info['id'])

    path = environ['PATH_INFO']
    pubId = path.replace('/es/publicacion/', '')
    reaccion_user_post = []
    # check if la publicacion existe, si no -> 404
    try:
        pubId = int(pubId)
        post = get_posts(id=pubId)
        if post == []:
            return handle_404

    except ValueError:
        return handle_404

    comments_list = get_comments(publicacionid=pubId)
    likesCount = get_likes_count(publicacionid=pubId)
    post = post[0]

    print("post : ", post)
    print("comments_list : ", comments_list)
    print("likesCount : ", likesCount)

    # verify if the user is conected, if yes verify if he reacionado a la publicacion
    if user_info:
        reaccion_user_post = get_like(publicacionid=pubId, userid=user_info['id'])

    response = publicacion.render(user_info=user_info, post=post, likesCount=likesCount,
                                  comments_list=comments_list, reaccion_user_post=reaccion_user_post,
                                  css_name='publicacion.css').encode(
        'utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]


# Helper functions for handling like and dislike actions
def handle_like_action(publication_id, user_id):
    existing_reaction = get_like(publicacionid=publication_id, userid=user_id)

    if existing_reaction:
        # The user already has a reaction, so we need to toggle it
        if existing_reaction[0]['likecount'] == 1:
            # User liked before, now toggle to delete the like
            delete_like(existing_reaction[0]['id'])
        else:
            # User disliked before, now toggle to like
            update_like(existing_reaction[0]['id'], 1)
    else:
        # The user has no previous reaction, so insert a new like
        insert_likes_data(publication_id=publication_id, user_id=user_id, like_count=1)


def handle_dislike_action(publication_id, user_id):
    existing_reaction = get_like(publicacionid=publication_id, userid=user_id)

    if existing_reaction:
        # The user already has a reaction, so we need to toggle it
        if existing_reaction[0]['likecount'] == 0:
            # User disliked before, now toggle to delete the dislike
            delete_like(existing_reaction[0]['id'])
        else:
            # User liked before, now toggle to dislike
            update_like(existing_reaction[0]['id'], 0)
    else:
        # The user has no previous reaction, so insert a new dislike
        insert_likes_data(publication_id=publication_id, user_id=user_id, like_count=0)


def page_competiciones(environ, start_response):
    global user_info
    competiciones_list = get_leagues()
    print(competiciones_list)
    response = competiciones.render(user_info=user_info, competiciones_list=competiciones_list, css_name='competiciones.css').encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]


def page_equipos(environ, start_response):
    global user_info
    equipos_list = get_teams()
    leagues_list = get_leagues()
    response = equipos.render(user_info=user_info, equipos_list=equipos_list, leagues=leagues_list, css_name='equipos.css').encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]


def page_partidos(environ, start_response):
    global user_info
    events = get_events()
    scores = get_points()
    leagues = get_leagues()
    estadios = get_stadiums()
    response = partidos.render(user_info=user_info, events=events, scores=scores, leagues=leagues, estadios=estadios, css_name='eventos.css').encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]


def page_sign_in(environ, start_response):
    global user_info
    user_info = is_user_logged_in(environ)
    flash_manager = FlashMessageManager()
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    redirect_location = None

    if environ['REQUEST_METHOD'] == 'POST':
        form_data = parse_post_data(environ)
        input_email = form_data.get('email')
        password = form_data.get('password')

        if (verify_user_login(str(input_email[0]), str(password[0]))) is not None:
            print("ACCESS GRANTED")

            user = get_users(correo=str(input_email[0]))
            cookie = cookies.SimpleCookie()

            # Configurar la cookie de usuario
            cookie['id'] = user[0]['id']
            cookie['username'] = user[0]['nombre']
            cookie['password'] = user[0]['contrasena']

            # Obtener la representación de cadena de la cookie
            cookie_string = cookie.output()

            # Agregar la cookie a las cabeceras de respuesta
            response_headers.append(('Set-Cookie', cookie_string))
            user_info['username'] = user[0]['nombre']
            user_info['id'] = user[0]['id']
            user_info['email'] = user[0]['correo']
            # Redirigir al usuario a la página de inicio
            redirect_location = '/es/inicio'
        else:
            flash_manager.add_message("El usuario o contraseña no existen.", "error")
            print("ACCESS DENIED")

    if redirect_location:
        response_headers.append(('Location', redirect_location))
        status = '302 Found'
    response = sign_in.render(css_name='login.css', flash_messages=flash_manager.get_messages(), user_info=user_info).encode('utf-8')
    start_response(status, response_headers)
    return [response]

# Global variables for password recovery


verification_code = 0
email = None


def page_forgot_password(environ, start_response):
    flash_manager = FlashMessageManager()
    global verification_code
    global email
    verification_code = generate_verification_code()
    status = '200 OK'
    if environ['REQUEST_METHOD'] == 'POST':
        form_data = parse_post_data(environ)
        email = form_data.get('email')

        users = get_users(correo=email)

        if users is not None:
            status = '302 Found'
            response_headers = [('Location', '/recuperar_contrasena/code')]
            # Envía el código de verificación por correo electrónico
            send_email(email, verification_code)
        else:
            flash_manager.add_message("No existe usuario con este email", "error")
            print("No existe usuario con este email")
    else:
        # En caso de que no sea una solicitud POST, mantener el estado 200 OK
        status = '200 OK'
        response_headers = []
    response = forgot_pass.render(flash_messages=flash_manager.get_messages()).encode('utf-8')
    start_response(status, response_headers)
    return [response]


def page_code(environ, start_response):
    response = forgot_pass_code.render().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    if environ['REQUEST_METHOD'] == 'POST':
        form_data = parse_post_data(environ)
        code_list = form_data.get('code')
        code = str(code_list[
                       0])  # Hay que convertirlo porque un formulario puede tener varios valores por eso devuelve una lista

        if verification_code == code:
            status = '302 Found'
            response_headers = [('Location', '/recuperar_contrasena/set_new_pass')]
        else:
            status = '200 OK'
            response = []

    start_response(status, response_headers)
    return [response]


def set_new_password(environ, start_response):
    flash_manager = FlashMessageManager()
    response = set_new_pass.render(flash_messages=flash_manager.get_messages()).encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    if environ['REQUEST_METHOD'] == 'POST':
        form_data = parse_post_data(environ)
        password = form_data.get('password')
        confirm_password = form_data.get('confirm_password')

        if password == confirm_password:
            update_passwd(str(email[0]), str(password[0]))
            response_headers.append(('Location', '/es/inicio'))
        else:
            status = '200 OK'
            flash_manager.add_message("Las contraseñas no coinciden.", "error")

    start_response(status, response_headers)
    return [response]


def page_sign_up(environ, start_response):
    flash_manager = FlashMessageManager()
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    if environ['REQUEST_METHOD'] == 'POST':
        # Obtengo los datos
        form_data = parse_post_data(environ)
        username = form_data.get('usuario')
        email = form_data.get('email')
        password = form_data.get('password')
        conf_passwd = form_data.get('rep-password')
        # Obtenemos los usuarios con el mismo correo
        users = get_users(correo=str(email[0]))
        # Si lista esta vacia
        if not users:
            # Compruebo que las contraseñas coinciden
            if str(password[0]) == str(conf_passwd[0]):
                insert_users_data(name=str(username[0]), password=str(password[0]), email=str(email[0]), isAdmin=False)
            else:
                flash_manager.add_message("Las contraseñas no coinciden.", "error")
        else:
            flash_manager.add_message("El correo ya está en uso.", "error")
            pass
    response = sign_up.render(css_name='login.css', flash_messages=flash_manager.get_messages()).encode('utf-8')
    start_response(status, response_headers)
    return [response]


def page_admin(environ, start_response):
    usuarios = get_users(correo="admin%40gmail.com", admin=True)
    print(f"{usuarios} fjhsjklnfsdjnvkj")
    admin_user = None

    if environ['REQUEST_METHOD'] == 'POST':
        form_data = parse_post_data(environ)
        email = form_data.get('email')
        password = form_data.get('password')

        admin_user = next(
            (user for user in usuarios if user['correo'] == email and user['contrasena'] == password and user['admin']),
            True)

    if admin_user:
        response_headers = [('Location', '/es/admin/crud/')]
        status = '302 Found'
        start_response(status, response_headers)
        return []
    response = admin.render(css_name='login.css').encode(
        'utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]


def page_crud(environ, start_response):
    # usuarios=get_users()
    competiciones = get_leagues()
    equipos = get_teams()
    players_list = get_players()
    print(players_list)
    partidos = get_events()
    publicaciones = get_posts()
    comments_list = get_comments()
    # likes_list = get_likes()

    # response = crud.render(usuarios=usuarios, competiciones=competiciones, equipos=equipos, partidos=partidos, comments_list=comments_list, publicaciones=publicaciones).encode('utf-8')
    response = crud.render(competiciones=competiciones, equipos=equipos, partidos=partidos,
                           comments_list=comments_list, publicaciones=publicaciones).encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]


def clear_cookie(cookie_name):
    cookie = cookies.SimpleCookie()
    cookie[cookie_name] = ''
    # Establecer una fecha de expiración en el pasado
    expiration_time = datetime.datetime.now() - datetime.timedelta(seconds=1)
    cookie[cookie_name]['expires'] = expiration_time.strftime('%a, %d %b %Y %H:%M:%S GMT')
    return cookie


def page_sign_out(environ, start_response):
    """Sign out the user"""
    global user_info
    user_info = {}
    response = logout.render().encode('utf-8')

    # Limpia las cookies de usuario
    clear_username_cookie = clear_cookie('username')
    clear_password_cookie = clear_cookie('password')
    cookie_string_username = clear_username_cookie.output()
    cookie_string_password = clear_password_cookie.output()
    response_headers = [('Set-Cookie', cookie_string_username), ('Set-Cookie', cookie_string_password),
                        ('Location', '/es/inicio')]
    status = '302 Found'
    start_response(status, response_headers)
    return [response]


def redirect_inicio(environ, start_response):
    """Redirect to the home page"""
    response_headers = [('Location', '/es/inicio')]
    start_response('302 Found', response_headers)
    return []


def is_user_logged_in(environ):
    cookie = cookies.SimpleCookie()
    cookie.load(environ.get('HTTP_COOKIE', ''))

    if 'username' in cookie and 'password' in cookie:
        # You can check if the username and password are valid
        username = cookie['username'].value
        password = cookie['password'].value
        return {username, password}
    else:
        return {}


def parse_post_data(environ):
    from urllib.parse import parse_qs
    data = environ['wsgi.input'].read(int(environ.get('CONTENT_LENGTH', 0))).decode('utf-8')
    form_data = parse_qs(data)
    return form_data


def serve_static(environ, start_response, path):
    # Set content type for CSS
    if path.endswith('.css'):
        content_type = 'text/css'
    else:
        content_type = 'text/plain'

    try:
        with open('.' + path, 'rb') as file:
            response_body = file.read()
        status = '200 OK'
    except FileNotFoundError:
        response_body = b'File Not Found'
        status = '404 Not Found'

    response_headers = [('Content-type', content_type)]
    start_response(status, response_headers)
    return [response_body]


def serve_static_img(environ, start_response, path):
    # Set the appropriate content type for CSS
    if path.endswith('.png'):
        content_type = 'image/png'
    else:
        content_type = 'text/plain'

    try:
        with open('.' + path, 'rb') as file:
            response_body = file.read()
        status = '200 OK'
    except FileNotFoundError:
        response_body = b'File Not Found'
        status = '404 Not Found'

    response_headers = [('Content-type', content_type)]
    start_response(status, response_headers)
    return [response_body]


def serve_static_js(environ, start_response, path):
    # Set the appropriate content type for JavaScript files
    if path.endswith('.js'):
        content_type = 'application/javascript'
    else:
        content_type = 'text/plain'

    try:
        with open('.' + path, 'rb') as file:
            response_body = file.read()
        status = '200 OK'
    except FileNotFoundError:
        response_body = b'File Not Found'
        status = '404 Not Found'

    response_headers = [('Content-type', content_type)]
    start_response(status, response_headers)
    return [response_body]


def handle_404(environ, start_response):
    response = error.render().encode('utf-8')
    status = '404 Not Found'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]
