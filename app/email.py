from flask import current_app, url_for, render_template
from flask_mail import Message

from app import mail
from app.api.tokens import generate_confirmation_token
from app.api.users import User
from config import Config

# building the server to send the email on
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

    token = generate_confirmation_token(user_email)
    confirm_url = url_for(
        'auth.confirm_email',
        token=token,
        _external=True,
    )

    txt  = render_template('email/confirmation.txt', confirm_url=confirm_url)
    html = render_template('email/confirmation.html', confirm_url=confirm_url)

    send_email("Welcome to Mindful (Please confirm your email!)", user_email, txt, html)

def send_password_reset_email(user):

    token = user.get_reset_password_token()
    reset_url = url_for(
        'auth.reset_password',
        token=token,
        _external=True,
    )

    txt = render_template('email/reset_password.txt', reset_url=reset_url, user=user)
    html = render_template('email/reset_password.html', reset_url=reset_url, user=user)

    send_email('[Mindful] Reset Your Password', user.email, txt, html)