from server import login

from ..model import Base
from .. import db

from ..auth.errors import bad_request

from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

class User(Base):

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
        return '<User /api/users/{0}>'.format(self.id)

    def set_password(self, new_pass):
        self.password_hash = generate_password_hash(new_pass)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self, include_email=False):

        data = {
            'id'    : self.id,
            'first' : self.first,
            'last'  : self.last
        }

        if include_email:
            data['email'] = self.email

        data['_links'] = {
            'self' : url_for('api.get_user', id=self.id)
        }

        return data

    def from_dict(self, data, new_user=False):
        for field in ['email', 'first', 'last']:
            if field in data:
                setattr(self, field, data[field])

        if new_user and 'password' in data:
            self.set_password(data['password'])

    def get_token(self, expires_in=3600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({ 'id' : self.id })

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None

        user = User.query.get(data['id'])
        return user

@login.user_loader
def get_user(id):
    return User.query.filter_by(id=id).first()
