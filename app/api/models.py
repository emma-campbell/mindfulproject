import base64
from datetime import datetime
import json, os
from time import time

from app import db, login

from flask import current_app, url_for
from flask_login import UserMixin
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash

import jwt

class User(UserMixin, db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    first = db.Column(db.String)
    last = db.Column(db.String)
    email = db.Column(db.String(120), index=True, unique=True)
    social_id = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    confirm_sent_on = db.Column(db.DateTime, nullable=True)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True,)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    _links = {
        "self" : "/api/users/{0}".format(id)
    }

    def __repr__(self):
        return '< USER /api/users/{0} >'.format(self.id)

    def set_password(self, new_password):
        self.password_hash = generate_password_hash(new_password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode({
            'reset_password' : self.id,
            'exp'            : time() + expires_in
        }, current_app.config['SECRET_KEY'],
                          algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_password_reset_token(token):
        try:
            id = jwt.decode(token,current_app.config['SECRET_KEY'],
                            algorithms=['HS256']['reset_password'])
        except:
            return

        return User.query.get(id)

    def to_dict(self, include_email=False):

        data = {
            'id'    : self.id,
            'first' : self.first,
            'last'  : self.last
        }

        if include_email:
            data['email'] = self.email

        data['_links'] = {
            "self" : url_for('api.get_user', id=self.id)
        }
        return data

    def from_dict(self, data, new_user=False):

        for field in ['username', 'email', 'about_me']:
            if field in data:
                setattr(self, field, data[field])

        if new_user and 'password' in data:
            self.set_password(data['password'])

    def get_token(self, expires_in=3600):

        now = datetime.utcnow()

        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token

        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)

        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
