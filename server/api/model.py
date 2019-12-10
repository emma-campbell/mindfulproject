from . import db
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base(object):

    id = db.Column(db.Integer, primary_key=True, unique=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def create(self):
        """Create new tuple"""
        db.session.add(self)
        db.session.commit()

    def save(self):
        """Save updated tuple"""
        db.session.commit()

    @staticmethod
    def get_all():
        return Base.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<{0}:{1}>'.format(cls.__name__.upper(), self.id)
