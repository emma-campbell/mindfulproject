from app.extensions import db, auth
from ..errors import bad_request

from flask import url_for, current_app

from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

class User(db.Model):

    # Basic User info
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String())

    # social_id is where we store oauth token
    social_id = db.Column(db.String(64), unique=True)

    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True,)

    roles = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, server_default='true')


    @classmethod
    def __repr__(self):
        return '<{0}:{1}>'.format(__name__.upper(), self.id)

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, email):
        return cls.query.filter_by(email=email).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def create(self):
        """Create new tuple"""
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError:
            return bad_request('Email already exists in our system! Please choose another.')

    def save(self):
        """Save updated tuple"""
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def is_valid(self):
        return self.is_active

    def to_dict(self, include_email=False):

        data = {
            'id'    : self.id,
            'name' : self.name,
        }

        if include_email:
            data['email'] = self.email

        data['_links'] = {
            'self' : url_for('api.get_user', id=self.id)
        }

        return data

    def from_dict(self, data, new_user=False):
        for field in ['email', 'name']:
            if field in data:
                setattr(self, field, data[field])

        if new_user and 'password' in data:
            self.password = auth.hash_password(data['password'])


    @staticmethod
    def check_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None

        return User.query.get(data['id'])
