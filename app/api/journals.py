from app import db
from datetime import date
from app.api.users import User

class Journal(db.Model):
    __tablename__ = "Journals"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    entry = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):

        data = {
            'id' : entry_id,
            'user_id'      : user_id,
            'entry'        : entry,
            'timestamp'    : timestamp,
        }

        return data

    def from_dict(self, data):

        for field in ['id', 'user_id', 'entry', 'timestamp']:
            if field in data:
                setattr(self, field, data[field])
