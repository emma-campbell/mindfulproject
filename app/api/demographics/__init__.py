from app import db

class Demographics(db.Model):

    user_id = db.Column(db.Integer, foreign_key=True, primary_key=True)
    bday = db.Column(db.DateTime)
    race = db.Column(db.String)
    gender = db.Column(db.String)
    orientation = db.Column(db.String)
    diagnosis = db.Column(db.Boolean)

    def to_dict(self):

        data = {
            'id' : user_id,
            'bday'        : bday,
            'race'        : race,
            'gender'      : gender,
            'orientation' : orientation,
            'diagnosis'   : diagnosis
        }

        return data

    def from_dict(self, data):

        for field in ['id', 'bday', 'race', 'gender', 'orientation', 'diagnosis']:
            if field in data:
                setattr(self, field, data[field])
