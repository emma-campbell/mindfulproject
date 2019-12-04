from app import db
from datetime import datetime
from app.api.users import User

class Journal(db.Model):
    __tablename__ = "Journals"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    title = db.Column(db.String(30))
    entry = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):

        data = {
            'id' : entry_id,
            'user_id'      : user_id,
            'title'        : title,
            'entry'        : entry,
            'timestamp'    : timestamp,
        }

        return data

    def from_dict(self, data):

        for field in ['id', 'user_id', 'title', 'entry', 'timestamp']:
            if field in data:
                setattr(self, field, data[field])
