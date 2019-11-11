from app import db, login

from flask_login import UserMixin
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    first = db.Column(db.String, index=True)
    last = db.Column(db.String, index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    access = db.Column(db.Integer)

    def __repr__(self):
        return '<USER {0}>'.format(self.id)

    def set_password(self, new_password):
        self.password_hash = generate_password_hash(new_password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_first(self, first):
        self.first = first

    def set_last(self, last):
        self.last = last

    def set_email(self, email):
        self.email = email

    def change_access(self, access):
        self.access = access

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
