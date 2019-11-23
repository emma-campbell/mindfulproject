'''
::module app.auth.oauth
::date 11-17-2019

Configuration of the google sign in
'''
import json
import urllib.request as urllib

from rauth import OAuth1Service, OAuth2Service
from flask import current_app, url_for, request, redirect, session
from flask_login import current_user, login_user

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

from app.auth import bp
from app import db
from app.api.models import User

class OAuthSignIn(object):
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials = current_app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']

    def authorize(self):
        pass

    def callback(self):
        pass

    def get_callback_url(self):
        return url_for('auth.oauth_callback', provider=self.provider_name, _external=True)

    @classmethod
    def get_provider(self, provider_name):
        if self.providers is None:
            self.providers = {}
            for provider_class in self.__subclasses__():
                provider = provider_class()
                self.providers[provider.provider_name] = provider
        return self.providers[provider_name]

class GoogleSignIn(OAuthSignIn):

    def __init__(self):
        super(GoogleSignIn, self).__init__('google')
        googleinfo = urllib.urlopen('https://accounts.google.com/.well-known/openid-configuration')
        google_params = json.load(googleinfo)
        self.service = OAuth2Service(
            name='google',
            client_id= self.consumer_id,
            client_secret= self.consumer_secret,
            authorize_url= google_params.get('authorization_endpoint'),
            base_url= google_params.get('userinfo_endpoint'),
            access_token_url= google_params.get('token_endpoint'),
        )

    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='email',
            response_type='code',
            redirect_uri=self.get_callback_url()))

    def callback(self):
        if 'code' not in request.args:
            return None, None, None
        oauth_session = self.service.get_auth_session(
            data={
                'code' : request.args['code'],
                'grant_type' : 'authorization_code',
                'redirect_uri' : self.get_callback_url()
            },
            decoder= json.loads
        )

        me = oauth_session.get('').json()
        names = me['name'].split(" ")
        return (names[0], names[1], me['email'])

@bp.route('/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@bp.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    oauth = OAuthSignIn.get_provider(provider)
    first, last, email = oauth.callback()

    if email is None:
        flask('Authentication failed.')
        return redirect(url_for('auth.register'))

    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(first=first, last=last, email=email)
        db.session.add(user)
        db.session.commit()

    login_user(user, remember=True)
    return redirect(url_for('main.index'))
