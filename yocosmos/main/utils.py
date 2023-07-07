from flask import request
from yocosmos import mail
from urllib.parse import urlparse, urljoin
from flask_mail import Message


# https://newbedev.com/how-do-i-get-a-is-safe-url-function-to-use-with-flask-and-how-does-it-work
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
        ref_url.netloc == test_url.netloc


def send_contact_email(name, email, message):
    msg = Message('Yo Cosmos contact form email',
                  sender='coffeeswirl27@gmail.com', recipients=['mthomsen3@gmail.com'])
    msg.body = f'''
    Name: {name}.
    Email: {email}.
    Messge: {message}.

    The End.
'''
    mail.send(msg)
