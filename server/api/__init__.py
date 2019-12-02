from flask import Blueprint
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from application import db

api = Blueprint('api', __name__, url_prefix='/api')

@as_declarative()
class Base(object):

    @declared_attr
    def __tablename__(self, cls):
        return cls.__name__.lower()

    def create(self):
        """Create new tuple"""
        db.session.add(self)
        db.session.commit()

    def save(self):
        """Save updated tuple"""
        db.session.commit()
