def send_email(destinatary, verification_code):
    '''
        Esta def es utilizada para enviar emails cuando el usuario ha olvidado su contraseña.
        Ejemplo destinatario destinatario@gmail.com y el verification_code es para asegurarnos de que el
        usuario que esta intentando cambiar la contraseña es el verdadero dueño del email correspondiente
    '''
    from dotenv import load_dotenv
    import smtplib
    import os
    from email.message import EmailMessage

    load_dotenv()
    remitente = 'eusko_basket@donostipub.eus'
    destinatario = [destinatary]
    msg = f"Si has olvidado tu contraseña, tu código de verficación es: {verification_code}"

    email = EmailMessage()
    email['From'] = remitente
    email['To'] = destinatario
    email['Subject'] = "Verification Code"
    email.set_content(msg)

    try:
        s = smtplib.SMTP_SSL('donostipub-eus.correoseguro.dinaserver.com')
        s.login(os.getenv('EMAIL_USERNAME'), os.getenv('EMAIL_PASSWORD'))
        s.sendmail(remitente, destinatario, email.as_string())
        s.quit()

        # print("Email sended!!!")
    except smtplib.SMTPException as e:
        print(f"Exception: {e}")


def generate_verification_code():
    from random import randint
    '''
        Devuelve el verification_code en formato de "cadena de caracteres"
    '''
    length = 8
    verification_code = []
    for i in range(length):
        verification_code.append(randint(0, 9))
        verification_code[i] = str(verification_code[i])
    return "".join(verification_code)


def get_user_cookie():
    from http import cookies  # Obtener la cookie de usuario
    cookie = cookies.SimpleCookie()
    user_cookie = [cookie.get('username'), cookie.get('password')]

    if user_cookie:
        return user_cookie.value
    else:
        return None
