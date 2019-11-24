from threading import Thread
from flask import current_app, url_for, render_template
from flask_mail import Message
from app import mail

from itsdangerous import URLSafeTimedSerializer

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body

    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()


def send_confirmation_email(user_email):
    confirm_serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

    confirm_url = url_for(
        'auth.confirm_email',
        token=confirm_serializer.dumps(user_email, salt='email-confirmation-salt'),
        _external=True)

    txt  = render_template('email/confirmation.txt', confirm_url=confirm_url)
    html = render_template('email/confirmation.html', confirm_url=confirm_url)

    send_email("Welcome to Mindful [PLEASE CONFIRM YOUR EMAIL]", current_app.config['MAIL_USERNAME'], user_email, txt, html)
