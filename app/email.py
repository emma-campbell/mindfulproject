import time
from threading import Thread
from flask import current_app, url_for, render_template
from flask_mail import Message
from app import mail
from config import Config
from itsdangerous import URLSafeTimedSerializer

import smtplib, ssl
from smtplib import SMTPAuthenticationError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, to, txt, html):

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = Config.MAIL_USERNAME

    message.attach(MIMEText(txt, 'plain'))
    message.attach(MIMEText(html, 'html'))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL (Config.MAIL_SERVER, Config.MAIL_PORT,
                           context=context) as server:
        server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
        server.sendmail(
            Config.MAIL_USERNAME, to, message.as_string()
        )

def send_confirmation_email(user_email):
    confirm_serializer = URLSafeTimedSerializer(Config.SECRET_KEY)

    confirm_url = url_for(
        'auth.confirm_email',
        token=confirm_serializer.dumps(user_email, salt='email-confirmation-salt'),
        _external=True)

    txt  = render_template('email/confirmation.txt', confirm_url=confirm_url)
    html = render_template('email/confirmation.html', confirm_url=confirm_url)

    send_email("Welcome to Mindful [PLEASE CONFIRM YOUR EMAIL]", user_email,txt,  html)
